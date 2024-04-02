# uvicorn main:app --reload  --> WAS 실행
# main:app -> main의 app을 실행하라
# reload   -> 코드 변경 시 자동으로 다시 켜줌(저장 시)

import uvicorn

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello FastAPI!"
    }