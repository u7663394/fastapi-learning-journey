from fastapi import FastAPI, Query

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. 查询参数: skip, limit
@app.get("/news/list")
async def get_news_list(skip: int = Query(0, description="The number of items to skip (default is 0).", ge=0), 
                        limit: int = Query(10, description="The number of items to return (default is 10).", lt=100)):
  return {"skip": skip, "limit": limit}