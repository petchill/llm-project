
from flask import Blueprint

# The first argument 'api' is the blueprint's name.
# The second argument, __name__, helps Flask locate the blueprint's root path.
api = Blueprint('api', __name__)

# Import the routes to register them with the blueprint
from . import routes
