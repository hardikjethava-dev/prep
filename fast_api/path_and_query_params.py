from fastapi import FastAPI

app = FastAPI() # initializes the ASGI application

@app.get("/users/{user_id}")
def get_user(user_id: int, active: bool = True): #FastAPI validates input before entering business logic
    return {
        "user_id": user_id,
        "active": active
    }