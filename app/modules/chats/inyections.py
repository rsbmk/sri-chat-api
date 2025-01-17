from app.core.db import Store
from app.modules.chats.query import QueryRepository
from app.modules.chats import ChatService

store = Store()
queryRepository = QueryRepository(vector_store=store.get_vector_store())

chatService = ChatService(queryRepository=queryRepository)
