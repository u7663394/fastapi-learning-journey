from fastapi import FastAPI, Path

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. 访问: /book/{id}; 响应: {"id": id, "msg": "This is your {id} book"}
@app.get("/book/{id}")
async def get_book(id: int = Path(..., description="The ID of the book, must be between 1 and 100.", ge=1, le=100)):
    return {"id": id, "msg": f"This is your {id} book"}

# 3. 访问: /author/{name}; 响应: {"name": name, "msg": "This is {name}'s book"}
@app.get("/author/{name}")
async def get_author(name: str = Path(..., description="The name of the author, must be between 2 and 10 characters.", min_length=2, max_length=10)):
    return {"name": name, "msg": f"The author is {name}"}