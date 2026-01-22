from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # initializes the ASGI application

class UserCreate(BaseModel):
    email: str
    age: int

@app.post("/users")
def create_user(user: UserCreate):
    return user


# example request
# Valid Request
{
    "email": "test@gmail.com",
    "age": 25
}

# Invalid Request, automatically rejected with 422
# Unprocessable Content -> 422
{
  "email": "test@gmail.com",
  "age": "twenty"
}