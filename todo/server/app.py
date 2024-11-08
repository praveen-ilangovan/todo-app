"""
Todo Application
"""

# Builtin imports
from contextlib import asynccontextmanager

# Project specific imports
from fastapi import FastAPI

# Local imports
from .database import ToDoDb

#-----------------------------------------------------------------------------#
# App
#-----------------------------------------------------------------------------#

# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to the database
    db = ToDoDb()
    await db.connect()

    yield

    # Shutdown
    db.shutdown()


app = FastAPI(lifespan=lifespan)

#-----------------------------------------------------------------------------#
# Routes
#-----------------------------------------------------------------------------#

@app.get("/", tags=['Root'])
async def index() -> dict[str, str]:
    """
    HomePage
    """
    return {"message": "World's Best ToDo App!!"}
