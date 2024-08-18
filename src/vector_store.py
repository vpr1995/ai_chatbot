from langchain_huggingface import HuggingFaceEmbeddings
from uuid import uuid4
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from utils.logger import logger


class VectorStoreManager:
    def __init__(self, docs):
        self.docs = docs
        self.embeddings = HuggingFaceEmbeddings()
        self.persist_on_disk_path = "vector_store"
        self.index = faiss.IndexFlatL2(
            len(self.embeddings.embed_query("hello world")))
        self.uuids = None
        self.vector_store: FAISS

        try:
            logger.info("Attempting to load the vector store from disk...")
            self.vector_store = FAISS.load_local(
                self.persist_on_disk_path, self.embeddings,
                allow_dangerous_deserialization=True)
        except Exception as e:
            logger.warn(f"An error occurred: {e}\n\n"
                        "Creating a new vector store...")
            self.vector_store = FAISS(
                embedding_function=self.embeddings,
                index=self.index,
                docstore=InMemoryDocstore(),
                index_to_docstore_id={},
            )
        finally:
            logger.info("Vector store loaded successfully.")

    def add_documents(self):
        logger.info("Adding the documents to the vector store...")
        self.uuids = [str(uuid4()) for _ in range(len(self.docs))]
        self.vector_store.add_documents(
            documents=self.docs, ids=self.uuids)
        logger.info("Documents added successfully.")
        return self.vector_store

    def persist_on_disk(self):
        logger.info("Persisting the vector store on disk...")
        self.vector_store.save_local(self.persist_on_disk_path)
