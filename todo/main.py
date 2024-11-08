"""
Main entrypoint
"""

# Project specific imports
import uvicorn
from dotenv import load_dotenv

# Load the env file
load_dotenv()

def main():
    """Main function"""
    uvicorn.run("todo.server.app:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
