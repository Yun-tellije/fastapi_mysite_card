# uvicorn main:app --reload  --> WAS 실행
# main:app -> main의 app을 실행하라
# reload   -> 코드 변경 시 자동으로 다시 켜줌(저장 시)

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from backend.routes import kakao

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(kakao.router, prefix="/kakao")

@app.get("/") # http://127.0.0.1:8000
async def welcome(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})