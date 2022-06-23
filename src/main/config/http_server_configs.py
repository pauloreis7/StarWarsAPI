from fastapi import FastAPI

from src.main.routes import starship_routes

app = FastAPI()

app.include_router(starship_routes)
