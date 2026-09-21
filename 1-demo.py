from fastapi import FastAPI

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. Define a route for the root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

# 3. Run: uvicorn main:app --reload
#   - uvicorn: a server for running FastAPI applications
#   - main: refers to the filename
#   - app: refers to the FastAPI instance
#   - reload: enables automatic reloading of the server when code changes