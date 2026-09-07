from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api import routes

app = FastAPI(
    title="Glass Classification API",
    description="Glass type classified web application",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"),name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(routes.router)

@app.get("/")
async def root():
    return {
        "message": "Glass Classification API",
        "docs": "/docs",
        "version": "1.0.0"
    }

