from fastapi import FastAPI
from contextlib import asynccontextmanager
from player.routes import player_router
from fastapi.middleware.cors import CORSMiddleware
from db import client

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await client.admin.command("ping")
    except Exception:
        raise RuntimeError("MongoDB connection failed")
    yield
    await client.close()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "hello": "world"
    }

app.include_router(player_router)
