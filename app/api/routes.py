from . import api
from .chat import post_chat_with_agent_name


@api.route('/chat', methods=['POST'])
def post_chat():
    return post_chat_with_agent_name("")


@api.route('/chat/qa', methods=['POST'])
def post_qa():
    return post_chat_with_agent_name("Q&A")


@api.route('/chat/poem', methods=['POST'])
def post_poem():
    return post_chat_with_agent_name("poem generator")


@api.route('/chat/code', methods=['POST'])
def post_code():
    return post_chat_with_agent_name("coding assistant")


@api.route('/chat/tone', methods=['POST'])
def post_tone():
    return post_chat_with_agent_name("tone rewriter")
