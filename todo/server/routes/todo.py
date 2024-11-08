"""
Routes for ToDo List
"""

# Project specific imports
from fastapi import APIRouter, status

# Local imports
from ..models.todolist import ToDoList

#-----------------------------------------------------------------------------#
# Router
#-----------------------------------------------------------------------------#

router = APIRouter()

#-----------------------------------------------------------------------------#
# Routes
#-----------------------------------------------------------------------------#

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ToDoList)
async def create_todo_list(todolist: ToDoList) -> ToDoList:
    await todolist.insert()
    return todolist
