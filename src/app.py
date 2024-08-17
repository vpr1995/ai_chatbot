from uuid import uuid4
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from transformers import logging
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_ollama import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_core.chat_history import BaseChatMessageHistory

logging.set_verbosity(logging.CRITICAL)

class DocumentProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.loader = PyPDFLoader(file_path=self.file_path)
        self.docs = None

    def load_and_split(self):
        print("Loading the document...")
        self.docs = self.loader.load_and_split(
            text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        )
        print("Document loaded and split successfully.")
        return self.docs

class VectorStoreManager:
    def __init__(self, docs):
        self.docs = docs
        self.embeddings = HuggingFaceEmbeddings()
        self.index = faiss.IndexFlatL2(len(self.embeddings.embed_query("hello world")))
        self.vector_store = FAISS(
            embedding_function=self.embeddings,
            index=self.index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )
        self.uuids = [str(uuid4()) for _ in range(len(self.docs))]

    def add_documents(self):
        print("Adding the documents to the vector store...")
        self.vector_store.add_documents(documents=self.docs, ids=self.uuids)
        print("Documents added successfully.")
        return self.vector_store

class Chatbot:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.retriever = self.vector_store.as_retriever()
        self.llm = ChatOllama(model="llama3.1", temperature=0.5)
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
            "You are a customer support representative for question-answering tasks regarding installation and troubleshooting of garage door opener. "
            "Use the following pieces of retrieved manual to answer "
            "the question. If you don't know the answer, say you do not know. Rely on the manual as much as you can and keep the "
            "answer nice and informative. Also make sure to ask follow-up questions if needed. Provide answer in step by step format. Do not give any manual references because user might not have the manual with them."
            "\n\n"
            "{context}"
        )
        self.qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        self.question_answer_chain = create_stuff_documents_chain(self.llm, self.qa_prompt)
        self.rag_chain = create_retrieval_chain(self.history_aware_retriever, self.question_answer_chain)

        self.conversational_rag_chain = RunnableWithMessageHistory(
            self.rag_chain,
            self.get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )

    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()
        return self.store[session_id]

    def return_response(self, user_query):
        response = self.conversational_rag_chain.invoke(
            {"input": user_query},
            {"configurable": {"session_id": "session_1"}},
        )
        return response["answer"]

    def start_chat(self):
        print("=======================================================================")
        print("Conversational RAG Chatbot")
        print("=======================================================================")

        query = ""
        while query != "bye":
            query = input("\033[1m User >>: \033[0m")
            response = self.return_response(query)
            print(f"\033[1m Chatbot >>: \033[0m {response}")

if __name__ == "__main__":
    document_processor = DocumentProcessor(file_path="./files/3ef5a4_7f4ef254977c43bcb4bc6790d37ac0ff.pdf")
    docs = document_processor.load_and_split()

    vector_store_manager = VectorStoreManager(docs)
    vector_store = vector_store_manager.add_documents()

    chatbot = Chatbot(vector_store)
    chatbot.start_chat()