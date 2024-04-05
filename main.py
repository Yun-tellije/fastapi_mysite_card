# uvicorn main:app --reload  --> WAS 실행
# main:app -> main의 app을 실행하라
# reload   -> 코드 변경 시 자동으로 다시 켜줌(저장 시)

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/") # http://127.0.0.1:8000
async def welcome(request: Request) -> dict:
    return templates.TemplateResponse("index.html", {"request": request})