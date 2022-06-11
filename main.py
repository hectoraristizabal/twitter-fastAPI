# Models
from models import User,UserBase,UserLogin,Tweet

# FastAPI
from fastapi import FastAPI, status

# Pydantic
from pydantic import List

app = FastAPI()

# Path Operations

@app.get(path='/')
def home():
    return {'Twitter API':"Working!"}

## Users

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup():
    pass

@app.post(
    path="/loging",
    response_model=User,
    status_code=status.HTTP_200_CREATED,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_CREATED,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_CREATED,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_CREATED,
    summary="Deleted a User",
    tags=["Users"]
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user():
    pass

## Tweets


