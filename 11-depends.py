from fastapi import FastAPI, Depends, Query

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. Define dependency function
async def common_params(skip: int = Query(0, ge=0), 
                        limit: int = Query(10, le=60)):
  return {"skip": skip, "limit": limit}

# 3. Inject dependency into route
@app.get("/news")
async def get_news(res = Depends(common_params)):
  return res

@app.get("/users")
async def get_users(res = Depends(common_params)):
  return res