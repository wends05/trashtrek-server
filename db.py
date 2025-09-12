import os
from pymongo import AsyncMongoClient
from dotenv import load_dotenv

load_dotenv()
# Prefer explicit failure over implicit localhost fallback; also accept MONGODB_URI.
URI = os.getenv("MONGO_URI") or os.getenv("MONGO_URL")
if not URI:
    raise RuntimeError("MONGO_URI or MONGO_URL is not set. Please set MONGO_URI or MONGO_URL in the .env file.")

client = AsyncMongoClient(URI, serverselectiontimeoutms=5000, appname="trashtrek-api")

db = client["trashtrek"]

# Collections
players_collection = db.players
