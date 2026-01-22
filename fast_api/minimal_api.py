from fastapi import FastAPI

app = FastAPI() # initializes the ASGI application

@app.get("/health") # registers an HTTP GET route
def health_check():
    return {"status": "ok"} # return value is auto converted to json, no serialization code required 

