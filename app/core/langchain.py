import os
import getpass
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_mongodb import MongoDBChatMessageHistory
from langchain_openai import ChatOpenAI


def init_model():
    if not os.getenv("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass(
            "Enter API key for OpenAI: ")

    model = init_chat_model(
        "gpt-4o-mini", model_provider="openai", temperature=2.2, max_tokens=20)

    return model


llm_model = init_model()

mongo_conn_string = os.getenv("MONGODB_URI")
mongo_database = os.getenv("MONGODB_DATABASE")


def init_chain():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )
    chain = prompt | ChatOpenAI(
        model="gpt-4o",
        temperature=0,
    )

    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: MongoDBChatMessageHistory(
            session_id=session_id,
            connection_string=mongo_conn_string,
            database_name=mongo_database,
            collection_name="chat_histories",
        ),
        input_messages_key="question",
        history_messages_key="history",
    )

    return chain_with_history
