from pydantic import BaseModel, ValidationError
from flask import Flask, request, jsonify
from typing import TypedDict
import getpass
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass(
        "Enter API key for OpenAI: ")

model = init_chat_model("gpt-4o-mini", model_provider="openai")

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.get('/hello')
def GetHello():
    return 'Hello, World'


class UserPayload(TypedDict):
    name: str
    age: int


# Pydantic model for validation
class UserModel(BaseModel):
    name: str
    age: int


@app.post('/chat')
def PostChat():
    payload = request.get_json()
    message = payload['message']
    print(message)
    response = model.predict(message)
    return jsonify({
        "message": response
    })


@app.post('/user')
def PostHello():
    try:
        payload_dict = request.get_json()
        payload_model = UserModel(**payload_dict)
        payload: UserPayload = payload_model.dict()  # keeps the original TypedDict type
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400
    print(payload)
    return jsonify({
        "message": f"User {payload['name']} is {payload['age']} years old."
    })


@app.route('/page/<id>')
def petch(id):

    return 'Petch Page' + id


if __name__ == "__main__":
    app.run(debug=True)
