from fastapi import FastAPI, HTTPException

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. Exception handling (id only 1~6)
@app.get("/news/{id}")
async def get_news(id: int):
  id_list = [1, 2, 3, 4, 5, 6]
  # id not valid
  if id not in id_list:
    raise HTTPException(status_code=404, detail="News not found")
  # id valid
  return {"id": id, "content": f"This is the content of news {id}"}
