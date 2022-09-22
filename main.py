from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import text2emotion as te
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
    messages: list


def get_prominent_emotion(emotions: dict):
    largest_val = 0
    largest_key = ''
    for i, (key, value) in enumerate(emotions.items()):
        if value > largest_val:
            largest_val = value
            largest_key = key
    return largest_key


@app.post("/")
async def get_emotion(msgBody: MessageList):
    paragraph = '.'.join(msgBody.messages)
    print(paragraph)
    emotions = te.get_emotion(paragraph)
    emotion = get_prominent_emotion(emotions=emotions)
    print(emotion)
    return {'emotion': emotion, 'emotions': emotions}
