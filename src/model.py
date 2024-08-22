
from utils.logger import logger
from transformers import logging
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama import ChatOllama
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.history_aware_retriever import (
    create_history_aware_retriever
)
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory

logging.set_verbosity(logging.CRITICAL)


class Chatbot:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.retriever = self.vector_store.as_retriever()
        self.llm = ChatOllama(model="llama3.1", temperature=0.2)
        self.store = {}

        self.contextualize_q_system_prompt = (
            "Given a chat history and the latest user question "
            "which might reference context in the chat history, "
            "formulate a standalone question which can be understood "
            "without the chat history. Do NOT answer the question, "
            "just reformulate it if needed and otherwise return it as is."
        )
        self.contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        self.history_aware_retriever = create_history_aware_retriever(
            self.llm, self.retriever, self.contextualize_q_prompt
        )

        self.system_prompt = (
            "Context:\n"
            "You are a customer support representative for a garage door "
            "opener company.\n\n"

            "Objective:\n"
            "Answer customer questions about installation and troubleshooting "
            "of garage door openers accurately and concisely.\n\n"

            "Style:\n"
            "Professional and helpful customer service representative\n\n"

            "Tone:\n"
            "Friendly and informative.\n Never Change the tone of the "
            "conversation.\n\n"

            "Audience:\n"
            "Customers who have purchased or are using the company's garage "
            "door openers\n\n"

            "Response format:\n"
            "Provide instructions/answers in detailed bullet point format.\n"
            "Use only the information from the retrieved manual sections\n"
            "Do not reference the manual directly in your responses\n"
            "If the answer is not available in the provided information, state "
            "that you do not know\n\n"

            "Retrieved Manual:\n"
            "{context}"
        )

        self.qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        self.question_answer_chain = create_stuff_documents_chain(
            self.llm, self.qa_prompt)
        self.rag_chain = create_retrieval_chain(
            self.history_aware_retriever, self.question_answer_chain)

        self.conversational_rag_chain = RunnableWithMessageHistory(
            self.rag_chain,
            self.get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )

    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        return SQLChatMessageHistory(session_id,
                                     connection="sqlite:///messages.db")

    def return_response(self, user_query):
        response = self.conversational_rag_chain.invoke(
            {"input": user_query},
            {"configurable": {"session_id": "session_1"}},
        )
        return response["answer"]

    def start_chat(self, session_id="session_1"):
        print("====================================================")
        print("Conversational RAG Chatbot")
        print("====================================================")

        self.print_previous_chat(session_id)
        query = ""

        while query != "bye":
            query = input("\033[1m User >>: \033[0m")
            try:
                response = self.return_response(query)
                self.chatbot_message_print(response)
            except Exception as e:
                logger.error(f"An error occurred: {e}")
                self.chatbot_message_print(
                    "Sorry, I am unable to answer that question."
                    "Please try again.")

    def print_previous_chat(self, session_id):
        for message in self.get_session_history(session_id).messages:
            message = message.dict()

            if message["type"] == "human":
                self.human_message_print(message["content"])
            elif message["type"] == "ai":
                self.chatbot_message_print(message["content"])
            else:
                logger.error("Invalid message type")

    def human_message_print(self, message):
        print(f"\033[1m User >>: \033[0m {message}")

    def chatbot_message_print(self, message):
        print(f"\033[1m Chatbot >>: \033[0m {message}")
