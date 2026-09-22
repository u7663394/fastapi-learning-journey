from fastapi import FastAPI

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. 访问: /hello; 响应: {"msg": "Hello, FastAPI!"}
@app.get("/hello")
async def get_hello():
    return {"msg": "Hello, FastAPI!"}