from . import api
from .chat import PostChat


@api.route('/chat', methods=['POST'])
def post_chat():
    return PostChat()
