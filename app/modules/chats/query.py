from langchain_pinecone import PineconeVectorStore


class QueryRepository:
    vector_store: PineconeVectorStore

    def __init__(self, vector_store: PineconeVectorStore):
        self.vector_store = vector_store

    def similarity(self, query: str):
        return self.vector_store.similarity_search(query)
