from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec  # type: ignore

from app.core.config import settings
from app.core.constants import EMBEDDING_MODEL_NAME, BASE_URL_AZURE, INDEX_VECTOR_STORE
from app.decorators.singleton import singleton

import time


@singleton
class Store:
    pinecone: Pinecone
    embeddings: OpenAIEmbeddings
    vector_store: PineconeVectorStore
    index_name = INDEX_VECTOR_STORE

    def __init__(self):
        self.pinecone = Pinecone(api_key=settings.PINECODE_API_KEY)

        if not self.pinecone.has_index(self.index_name):
            index = self.pinecone.create_index(
                name=self.index_name,
                dimension=self.embeddings.embed_query("test").shape[0],
                # dimension=3072,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )

        while not self.pinecone.describe_index(self.index_name).status.ready:
            time.sleep(1)

        index = self.pinecone.Index(self.index_name)

        self.embeddings = OpenAIEmbeddings(
            model=EMBEDDING_MODEL_NAME,
            base_url=BASE_URL_AZURE,
            api_key=settings.OPENAI_API_KEY_GH,
        )
        self.vector_store = PineconeVectorStore(index=index, embedding=self.embeddings)

    def get_vector_store(self):
        return self.vector_store

    def get_pinecone(self):
        return self.pinecone

    def get_embeddings(self):
        return self.embeddings
