import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_mongodb import MongoDBChatMessageHistory
from langchain_openai import ChatOpenAI
from openai import BaseModel

mongo_conn_string = os.getenv("MONGODB_URI")
mongo_database = os.getenv("MONGODB_DATABASE")


def get_system_prompt_by_agent_name(agent_name):
    if agent_name == "Q&A":
        return "You are Q&A assistant. What You have to do is answer questions about the given context. You should answer as concisely as possible. If you don't know the answer."
    elif agent_name == "poem generator":
        return "You are a poem generator. What you have to do is generate a poem about the given topic and help user adjust to poem to be more beauty."
    elif agent_name == "coding assistant":
        return "You are a coding assistant. What you have to do is help user write the code and solve their problems in the most efficient way."
    elif agent_name == "tone rewriter":
        return "You are a tone rewriter. What you have to do is help use rewrite the tone of the given text to be more formal or informal. if user ask to do anything else, just say 'I don't know how to do that'."
    elif agent_name == "name and hobbies extractor":
        return "You have to summarize the user's paragraph and extract the name and hobbies of the user. If the user doesn't have any name or hobbies, just list the empty response."
    else:
        return "You are a helpful assistant."


class UserInfo(BaseModel):
    name: str
    hobbies: list[str]


def get_llm_by_agent_name(agent_name):
    if agent_name == "name and hobbies extractor":
        return ChatOpenAI(
            model="gpt-4",
            temperature=0,
        ).with_structured_output(UserInfo)
    else:
        return ChatOpenAI(
            model="gpt-4",
            temperature=0,
        )


def init_chain_with_agent(agent_name):
    system_prompt = get_system_prompt_by_agent_name(agent_name)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )
    llm = get_llm_by_agent_name(agent_name)
    chain = prompt | llm

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
