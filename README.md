# ToDo App

A simple todo application written using FastAPI, MongoDB, Motor and BeanieODM

## Running the application

Before running the application, create a .env file inside the todo-app and set the following environment variables

```sh
DB_URL="mongodb+srv://{USER}:{PWD}@cluster0.lzuie.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_USER_ID=""
DB_PASSWORD=""
DB_NAME=""
```

Install the dependencies and devDependencies and start the server.

```sh
cd todo-app
poetry install
poetry run start
```

This would start the application in http://127.0.0.1:8000/
