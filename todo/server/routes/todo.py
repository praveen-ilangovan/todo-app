"""
Routes for ToDo List
"""

# Builtin imports
from typing import List

# Project specific imports
from fastapi import APIRouter, status, HTTPException
from beanie import PydanticObjectId

# Local imports
from ..models.todolist import ToDoList

#-----------------------------------------------------------------------------#
# Router
#-----------------------------------------------------------------------------#

router = APIRouter()

#-----------------------------------------------------------------------------#
# Helpers
#-----------------------------------------------------------------------------#
async def get_todolist_by_id(id: PydanticObjectId) -> ToDoList:
    todolist = await ToDoList.get(id)
    if not todolist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"TodoList with {id} not found")
    return todolist

#-----------------------------------------------------------------------------#
# Routes
#-----------------------------------------------------------------------------#

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ToDoList)
async def create_todolist(todolist: ToDoList) -> ToDoList:
    await todolist.insert()
    return todolist

@router.get("/", response_model=List[ToDoList])
async def get_all_todolists() -> List[ToDoList]:
    todolists = await ToDoList.find_all().to_list()
    return todolists

@router.get("/{id}", response_model=ToDoList)
async def get_todolist(id: PydanticObjectId) -> ToDoList:
    todolist = await get_todolist_by_id(id)
    return todolist

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todolist(id: PydanticObjectId):
    todolist = await get_todolist_by_id(id)
    await todolist.delete()
    return {"message": "TodoList deleted successfully"}

