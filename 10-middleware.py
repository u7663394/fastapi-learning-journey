from fastapi import FastAPI

# 1. Create an instance of the FastAPI
app = FastAPI()

# 2. miidleware (sequence: from bottom to top)
@app.middleware("http")
async def middle_1(request, call_next):
  print("middle_1 start")
  response = await call_next(request)
  print("middle_1 end")
  return response

@app.middleware("http")
async def middle_2(request, call_next):
  print("middle_2 start")
  response = await call_next(request)
  print("middle_2 end")
  return response

@app.get("/")
async def root():
  return {"msg": "Hello FastAPI"}
