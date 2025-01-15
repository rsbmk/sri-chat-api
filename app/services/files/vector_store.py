from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore


class StoreEmbedder:
    embeddings: OpenAIEmbeddings
    vector_store: PineconeVectorStore

    def __init__(self, embeddings: OpenAIEmbeddings, vector_store: PineconeVectorStore):
        self.embeddings = embeddings
        self.vector_store = vector_store

    def load_embeddings_to_vector_store(self, docs: list[Document]) -> None:
        """
        Load a list of documents to the vector store by computing their embeddings and adding them.

        Args:
            docs: list of documents to add to the vector store
        """
        for doc in docs:
            embeddings = self.embeddings.embed_query(doc.page_content)
            self.vector_store.add_documents(documents=[doc], embeddings=embeddings)
