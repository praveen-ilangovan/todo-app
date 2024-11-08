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
from ..models.todoitem import ToDoItem

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

#-----------------------------------------------------------------------------#
# Routes - Item
#-----------------------------------------------------------------------------#

@router.post("/{id}/item", response_model=ToDoList)
async def add_todoitem(id: PydanticObjectId, todoitem: ToDoItem) -> ToDoList:
    todolist = await get_todolist_by_id(id)
    _ = await todolist.update({"$push": {"items": todoitem}})
    updated_list = await todolist.get(id)
    return updated_list

"""
Update the name of the todolist

Get todolist
    only return undone item

Add an item
Set an item to done
Remove an item
"""
