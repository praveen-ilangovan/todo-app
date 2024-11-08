"""

"""

# Builtin imports
import os
from typing import Optional

# Project specific imports
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

# Local imports
from .models.todolist import ToDoList

class ToDoDb:
    def __init__(self):
        self.__client: Optional[AsyncIOMotorClient] = None

    async def connect(self) -> None:
        url = os.environ["DB_URL"].format(
            USER=os.getenv("DB_USER_ID"), PWD=os.getenv("DB_PASSWORD")
        )

        self.__client = AsyncIOMotorClient(url)

        await init_beanie(
            database=self.__client.get_database( os.getenv("DB_NAME", "todoDb") ),
            document_models=[ToDoList]
        )

    def shutdown(self) -> None:
        self.__client.close()
