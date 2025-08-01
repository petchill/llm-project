from flask import Flask, request, jsonify

from app.core.langchain import init_chain_with_agent


def post_chat_with_agent_name(agent_name):
    payload = request.get_json()
    session_id = payload['session_id']
    message = payload['message']
    config = {"configurable": {"session_id": session_id}}
    chain = init_chain_with_agent(agent_name)
    response = chain.invoke({"question": message}, config=config)
    print(response)
    return jsonify({
        "message": response.content
    })


def post_chat_name_and_hobbies():
    payload = request.get_json()
    session_id = payload['session_id']
    message = payload['message']
    config = {"configurable": {"session_id": session_id}}
    chain = init_chain_with_agent("name and hobbies extractor")
    response = chain.invoke({"question": message}, config=config)
    print(response)
    return jsonify({
        "name": response.name,
        "hobbies": response.hobbies
    })
