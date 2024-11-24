from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
  return {
    "Message": "Bem vindo a minha primeira API com FastAPI"
  }
