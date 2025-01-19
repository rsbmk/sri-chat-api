from typing import List, TypedDict

from langchain_core.messages import (
    HumanMessage,
    AnyMessage,
)
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, END, StateGraph
from uuid import uuid4

from app.modules.chats.model import ChatModel
from app.modules.chats.trimmer import MessageTrimmer
from app.modules.chats.query import QueryRepository
from app.modules.chats.dto import InputDTO
from app.modules.chats.prompts_templates import prompt_template

memory = MemorySaver()


class State(TypedDict):
    question: str
    messages: List[AnyMessage]


class ChatService:
    def __init__(self, queryRepository: QueryRepository):
        self.model = ChatModel()
        self.trimmer = MessageTrimmer(self.model.get_model())
        self.queryRepository = queryRepository

        self.workflow = StateGraph(state_schema=State)
        self.workflow.add_edge(START, "model")
        self.workflow.add_node("model", self.call_model)
        self.workflow.add_edge("model", END)
        self.app = self.workflow.compile(checkpointer=memory)

    async def call_model(self, state: State):
        trimmed_messages = self.trimmer.invoke(state["messages"])
        context = self.queryRepository.similarity(state["question"])

        prompt = prompt_template.invoke(
            {
                "messages": trimmed_messages,
                "question": state["question"],
                "context": context,
            }
        )

        response = await self.model.ainvoke(prompt)
        return {"messages": response}

    async def input(self, data: InputDTO):
        thread_id = data.thread_id

        response = await self.app.ainvoke(
            {
                "messages": [HumanMessage(content=data.input)],
                "question": data.input,
            },
            config={"configurable": {"thread_id": thread_id}},
        )

        lastMessage = response["messages"]

        return {
            "content": lastMessage.content,
            "id": lastMessage.id,
            "thread_id": thread_id,
        }
