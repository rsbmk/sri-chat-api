from langchain_core.messages import trim_messages


class MessageTrimmer:
    def __init__(self, model):
        self.trimmer = trim_messages(
            max_tokens=2000,
            strategy="last",
            token_counter=model,
            include_system=True,
            allow_partial=False,
            start_on="human",
        )

    def invoke(self, messages):
        return self.trimmer.invoke(messages)
