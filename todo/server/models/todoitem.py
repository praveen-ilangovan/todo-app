"""
Model defining a simple todo item
"""

# Project specific imports
from pydantic import BaseModel

class ToDoItem(BaseModel):
    message: str
    is_done: bool = False
