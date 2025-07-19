from flask import Flask
# from .config import Config


def create_app():
    """
    Creates and configures a Flask application instance.
    This is the application factory.
    """

    app = Flask(__name__)

    # 1. Load configuration from the config object
    # app.config.from_object(Config)

    # 2. Import and register the API blueprint
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # Add a simple health check route
    @app.route('/health')
    def health_check():
        return "OK", 200

    return app
