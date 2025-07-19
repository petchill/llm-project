from flask import Flask, request, jsonify

from app.core.langchain import llm_model
from app.core.langchain import init_chain


def PostChat():
    payload = request.get_json()
    session_id = payload['session_id']
    message = payload['message']
    config = {"configurable": {"session_id": session_id}}
    chain = init_chain()
    response = chain.invoke({"question": message}, config=config)
    print(response)
    return jsonify({
        "message": response.content
    })
