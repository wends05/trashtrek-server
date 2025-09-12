from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from player.routes import player_router
from fastapi.middleware.cors import CORSMiddleware
from db import client
from logger import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting application...")
    try:
        await client.admin.command("ping")
    except Exception:
        raise RuntimeError("MongoDB connection failed")
    yield
    logger.info("Closing MongoDB connection...")
    await client.close()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response

@app.get("/")
def root():
    return {
        "hello": "world"
    }

app.include_router(player_router)
