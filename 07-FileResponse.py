from fastapi import FastAPI
from fastapi.responses import FileResponse

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. response with FileResponse
@app.get("/file")
async def get_file():
  my_path = "http://example.com/example.png"
  return FileResponse(my_path)