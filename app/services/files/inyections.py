from app.services.files import FilesService, DocumentLoader, StoreEmbedder
from app.db import Store

store = Store()
store_embedder = StoreEmbedder(
    embeddings=store.get_embeddings(), vector_store=store.get_vector_store()
)

service = FilesService(documentLoader=DocumentLoader(), store_embedder=store_embedder)
