from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. response with HTMLResponse
@app.get("/html", response_class=HTMLResponse)
async def get_html():
  return "<h1>HTML Content</h1>"