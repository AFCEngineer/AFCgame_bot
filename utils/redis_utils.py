# utils/redis_utils.py
import redis
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file locally (not needed on Railway)

# Connect to Redis
r = redis.from_url(os.getenv("REDIS_URL"))

def save_game(chat_id, game_state):
    r.set(f"game:{chat_id}", json.dumps(game_state))

def load_game(chat_id):
    data = r.get(f"game:{chat_id}")
    return json.loads(data) if data else None

def delete_game(chat_id):
    r.delete(f"game:{chat_id}")
