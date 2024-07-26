from fastapi import FastAPI
from app.database.config import engine
from app.api.models.tables import Base
from starlette.responses import RedirectResponse
from app.api.routers.endpoints import router
from starlette.middleware.cors import CORSMiddleware

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def main():
    return RedirectResponse("/docs")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
