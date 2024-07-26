from fastapi import FastAPI
from app.database.config import engine
from app.api.models.tables import Base
from starlette.responses import RedirectResponse
from app.api.routers.endpoints import router

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def main():
    return RedirectResponse("/docs")


app.include_router(router)
