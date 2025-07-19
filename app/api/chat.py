from flask import Flask, request, jsonify

from app.core.langchain import llm_model


def PostChat():
    payload = request.get_json()
    message = payload['message']
    print(message)
    response = llm_model.predict(message)
    return jsonify({
        "message": response
    })
