from model import Chatbot
from vector_store import VectorStoreManager
from document_loader import DocumentProcessor

if __name__ == "__main__":
    document_processor = DocumentProcessor(
        directory_path="files/")
    docs = document_processor.load_and_split()

    vector_store_manager = VectorStoreManager(docs)
    vector_store = vector_store_manager.add_documents()
    vector_store_manager.persist_on_disk()

    chatbot = Chatbot(vector_store)
    chatbot.start_chat()
