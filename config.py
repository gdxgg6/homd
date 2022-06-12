## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCz4lp67NVw5vacVBbDQeV2k7OpaQY5TbqQK9o3ZpuZQmVo2HC3w17NhaTMYHzUOM6BRcrpSgqaaFs8XhcuG1H6Y4lOvzztFVs3Y5yqOjAmq65DWUktZ5MRYZRbEaCFFHb2daX9Ri1NUmUSWkWxde9qYOQliuoGcUPXiPhMWc0aZvNUXFpH0hD-6ApXJxmtkFKKMegx4g3Ej0yH22K6Dxj1QbDyph3qHxzvI29PZsC9LXPgCeKdFhucicxj3AXxiPDaGndtvfo1j4Pkbg8jFrpV7YpCEvGAZ-_AOsqfqr3dDjx93S9HAKaHVQqE6QFwakjcJqgxVvNNyUrl4S-nRqKyAAAAATnj-fIA")
BOT_TOKEN = getenv("BOT_TOKEN", "5291911297:AAHnpl6x5K3SLpluuUBuNu1a5nSkwKnU1Vk")
BOT_NAME = getenv("BOT_NAME", "Music bot")
API_ID = int(getenv("API_ID", "13595786"))
API_HASH = getenv("API_HASH", "e326248b4b66384f067f6b18f98c0030")
OWNER_NAME = getenv("OWNER_NAME", "Mhamd")
OWNER_USERNAME = getenv("OWNER_USERNAME", "FYFFYF")
ALIVE_NAME = getenv("ALIVE_NAME", "Mhamd")
BOT_USERNAME = getenv("BOT_USERNAME", "ne_2bot")
OWNER_ID = getenv("OWNER_ID", "5290103349")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Music")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "vvbha")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kzzgg")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5290103349").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
