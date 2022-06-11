# Models
import json
from unittest import result
from models import User,UserBase,UserLogin,Tweet, UserRegister

# FastAPI
from fastapi import Body, FastAPI, status

# Pydantic
from typing import List

app = FastAPI()

# Path Operations

## Users

### Register a user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
    """
    Signup

    This path operation creates an user in the app

    Parameters:
    - Request body parameter
        - user: UserRegister

    Returns a json with the basic user information:
    - user_id: UUID
    - email: Emailstr
    - first_name: str
    - last_name: str
    - birth_date: date
    """
    with open("users.json","r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        # moverme al inicio
        f.seek(0)
        f.write(json.dumps(results))
        return user



### Login a user
@app.post(
    path="/loging",
    response_model=User,
    status_code=status.HTTP_200_OK  ,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

### Show all user
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    """
    Signup

    This path operation shows all users in the app

    Parameters:
    - 

    Returns a json with all users in the app, with the following keys:
    - user_id: UUID
    - email: Emailstr
    - first_name: str
    - last_name: str
    - birth_date: datime  
    """
    with open("users.json","r",encoding="utf-8") as f:
        results = json.loads(f.read())
        return results


### Show a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user():
    pass

### Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Deleted a User",
    tags=["Users"]
)
def delete_a_user():
    pass

### Update a user
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

### Show all tweets
@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]

    )
def home():
    return {'Twitter API':"Working!"}

### Show post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post():
    pass

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass