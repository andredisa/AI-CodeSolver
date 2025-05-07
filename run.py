import os
import sys
from app.main import app  # Assuming your main app is inside 'app/main.py'
import dotenv

def load_environment():
    """
    Load environment variables from .env file.
    """
    dotenv.load_dotenv()  # Load .env file if present

def run_server():
    """
    Run the Flask app on the local development server.
    """
    try:
        # Check if FLASK_APP is set in environment, otherwise set it to 'run.py'
        if not os.getenv('FLASK_APP'):
            os.environ['FLASK_APP'] = 'run.py'

        # Set the Flask environment to development for debugging purposes
        os.environ['FLASK_ENV'] = 'development'

        # Run the app on localhost at port 5000
        app.run(debug=True, host='0.0.0.0', port=5000)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    # Load environment variables from .env file
    load_environment()
    
    # Run the Flask server
    run_server()
