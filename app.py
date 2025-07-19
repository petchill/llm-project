# run.py

import os
from dotenv import load_dotenv
from app import create_app

# Load environment variables from .env file
load_dotenv()

# Create the Flask app instance using the app factory
app = create_app()

if __name__ == '__main__':
    port = os.getenv("PORT")
    if port is None:
        port = 5000
    # Run the app
    # Use debug=True for development to get auto-reloads and detailed error pages
    app.run(debug=True)
