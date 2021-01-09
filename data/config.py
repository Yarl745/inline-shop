import json
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

admins = json.loads(os.getenv("ADMIN_IDS"))

ip = os.getenv("ip")

PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_DB = os.getenv("PG_DB")
PG_PORT = os.getenv("PG_PORT")

POSTGRES_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{ip}:{PG_PORT}/{PG_DB}"

FONDY_ID = os.getenv("FONDY_ID")
FONDY_KEY = os.getenv("FONDY_KEY")