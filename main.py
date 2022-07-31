from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}

class MessageList(BaseModel):
    messages:list 



@app.post("/")
async def create_item(msgBody: MessageList):
    paragraph = ' '.join(msgBody.messages)
    print(paragraph)
    return {'emotion':"happy"}