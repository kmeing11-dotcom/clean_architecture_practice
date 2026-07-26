from fastapi import FastAPI
from app.api.v1.router import router
from contextlib import asynccontextmanager
from app.core.database import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Сервис работает!"}