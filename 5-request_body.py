from fastapi import FastAPI, Query
from pydantic import BaseModel

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. Define type for request body
class User(BaseModel):
  username: str
  userpwd: str

# 3. Post
@app.post("/register")
async def create_user(myUser: User):
  return {"username": myUser.username, "userpwd": myUser.userpwd}