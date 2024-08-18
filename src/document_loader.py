from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.logger import logger


class DocumentProcessor:
    def __init__(self, directory_path):
        self.file_path = directory_path
        self.loader = PyPDFDirectoryLoader(directory_path)
        self.docs = None

    def load_and_split(self):
        logger.info("Loading the document...")
        self.docs = self.loader.load_and_split(
            text_splitter=RecursiveCharacterTextSplitter(
                chunk_size=1000, chunk_overlap=100)
        )

        for doc in self.docs:
            doc.metadata["product_type"] = doc.metadata["source"].split(
                "/")[-2]
            doc.metadata["doc_type"] = doc.metadata["source"].split("/")[-3]
        logger.info("Document loaded and split successfully.")
        return self.docs
