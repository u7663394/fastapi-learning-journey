from fastapi import FastAPI
from pydantic import BaseModel, Field

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. Define type for response content
class News(BaseModel):
  id: int = Field(..., description="The ID of the news.")
  title: str = Field(..., description="The title of the news.")
  content: str = Field(..., description="The content of the news.")

# 3. Get
@app.get("/news/{news_id}", response_model=News) 
async def get_news(news_id: int):
  return {"id": news_id, "title": "FastAPI", "content": "Hello FastAPI!"}