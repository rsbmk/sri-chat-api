from pinecone import Pinecone, ServerlessSpec  # type: ignore
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from app.decorators.singleton import singleton
from app.config import settings

import time


@singleton
class Store:
    pinecone: Pinecone
    embeddings: OpenAIEmbeddings
    vector_store: PineconeVectorStore
    index_name = "langchain-documents-sri-chat"

    def __init__(self):
        self.pinecone = Pinecone(api_key=settings.PINECODE_API_KEY)

        if not self.pinecone.has_index(self.index_name):
            index = self.pinecone.create_index(
                name=self.index_name,
                # dimension=self.embeddings.embed_query("test").shape[0],
                dimension=3072,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )

        while not self.pinecone.describe_index(self.index_name).status.ready:
            time.sleep(1)

        index = self.pinecone.Index(self.index_name)

        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        self.vector_store = PineconeVectorStore(index=index, embedding=self.embeddings)

    def get_vector_store(self):
        return self.vector_store

    def get_pinecone(self):
        return self.pinecone

    def get_embeddings(self):
        return self.embeddings
