from fastapi import FastAPI

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. 访问: /book/{id}; 响应: {"id": id, "msg": "This is your {id} book"}
@app.get("/book/{id}")
async def get_book(id: int):
    return {"id": id, "msg": f"This is your {id} book"}
