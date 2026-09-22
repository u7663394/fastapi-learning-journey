from fastapi import FastAPI
from pydantic import BaseModel, Field

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. Define type for request body
class User(BaseModel):
  username: str = Field(default="Peter", description="The username of the user.")
  userpwd: str = Field(..., description="The password of the user.", min_length=5, max_length=20)

# 3. Post
@app.post("/register")
async def create_user(myUser: User):
  return {"username": myUser.username, "userpwd": myUser.userpwd}