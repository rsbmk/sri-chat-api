from langchain_openai import ChatOpenAI

from app.core.constants import INPUT_MODEL_NAME, BASE_URL_AZURE
from app.core.config import settings


class ChatModel:
    def __init__(self):
        self.model = ChatOpenAI(
            model=INPUT_MODEL_NAME,
            base_url=BASE_URL_AZURE,
            api_key=settings.OPENAI_API_KEY_GH,
        )

    async def ainvoke(self, prompt):
        return await self.model.ainvoke(prompt)

    async def astream(self, prompt):
        async for chunk in self.model.astream(prompt):
            yield chunk

    def get_model(self):
        return self.model
