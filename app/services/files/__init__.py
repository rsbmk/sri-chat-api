from fastapi import UploadFile, HTTPException

from app.services.files.vector_store import StoreEmbedder
from app.services.files.loader import DocumentLoader

import tempfile
import os


class FilesService:
    documentLoader: DocumentLoader
    store_embedder: StoreEmbedder

    def __init__(self, documentLoader: DocumentLoader, store_embedder: StoreEmbedder):
        """
        Initialize the FilesService class.

        Args:
            documentLoader (DocumentLoader): A DocumentLoader object to handle text files.
            store_embedder (StoreEmbedder): A StoreEmbedder object to add embeddings to the vector store.
        """
        self.store_embedder = store_embedder
        self.documentLoader = documentLoader

    async def validate_file_text(self, file: UploadFile):
        """
        Validate the uploaded file to ensure it is a .txt file and save its
        content to a temporary file.

        Args:
            file (UploadFile): The uploaded file to be validated and processed.

        Returns:
            str: The path to the temporary file where the content is saved.

        Raises:
            HTTPException: If the file is not a .txt file or has no filename.
        """

        if file.filename is None or not file.filename.endswith(".txt"):
            raise HTTPException(status_code=400, detail="Only .txt files are allowed")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
            temp_file_path = temp_file.name
            content = await file.read()
            temp_file.write(content)

        return temp_file_path

    def upload_file_text(self, file_path: str):
        """
        Load all documents from a single file into the vector store.

        Args:
            file_path: The path to the file to be loaded.

        Raises:
            HTTPException: If an error occurs while loading the file.
        """

        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")

        try:
            documents = self.documentLoader.file_text(file_path)
            self.store_embedder.load_embeddings_to_vector_store(documents)
        except Exception as e:
            raise Exception(f"Error loading file: {e}")
        finally:
            os.remove(file_path)
