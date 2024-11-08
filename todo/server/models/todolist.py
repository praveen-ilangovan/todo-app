"""
ToDoList
"""

# Project specific imports
from beanie import Document

# Local imports
from .todoitem import ToDoItem

class ToDoList(Document):
    name: str
    items: list[ToDoItem] = []

    class Settings:
        name = "todo_collection"

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Grocery",
                "items": [
                    {
                        "message": "Buy Apples",
                        "is_done": False
                    }
                ]
            }
        }