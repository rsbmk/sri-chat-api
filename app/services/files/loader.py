from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader


class DocumentSplitter:
    def __init__(self):
        pass

    def invoke(self, docs: list[Document]) -> list[Document]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200, add_start_index=True
        )
        return text_splitter.split_documents(docs)


class DocumentLoader:
    splitter: DocumentSplitter

    def __init__(self):
        self.splitter = DocumentSplitter()

    def file_text(self, file_path: str) -> list[Document]:
        """Load all documents from a single file."""
        loader = TextLoader(file_path)
        documents = self.splitter.invoke(loader.load())
        return documents
