import os
import getpass
from langchain.chat_models import init_chat_model


def init_model():
    if not os.getenv("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass(
            "Enter API key for OpenAI: ")

    model = init_chat_model("gpt-4o-mini", model_provider="openai")

    return model


llm_model = init_model()
