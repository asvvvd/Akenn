## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCoEn-YXL0FSzyFRlNUS61kwEpBFeH2_4UN-bdX5Ej1EXp1I0ko1qOlG9jyoSblUv_u8B6S6wroUGUq0OxKYL-gKY6ENVy5jC1_REpsgs9n-u1F60IYEV7Ye3JzURAtdiUoixZTwpBsJ6tj5jNmAQRnEo54bCPFEhg4dFDr1KA92P-AxOMAxNKYpqMoXw7YKlQx-VHBwGywZ8IIKtzVRxnTThAwPSxownvbRw3dL_vm9-L2ao3sHcx8YLnbKR9DT245wlFGLHG4asXN2FuhcBg5UINVgpVQZIGF_rDtn7Y1JJuLSMgOtjxCQSrjGljzPYKh6h62gqdYq7YWHSZRL-cDAAAAATfGhfgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5229626458:AAGj_DBOa3BXQnYaw_-WIqJFo-PjsZx6ap0")
BOT_NAME = getenv("BOT_NAME", "𝖥𝗅𝗈𝖱𝖾𝖷")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Aken")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ssstss")
ALIVE_NAME = getenv("ALIVE_NAME", "Aken")
BOT_USERNAME = getenv("BOT_USERNAME", "Mus_3Bot")
OWNER_ID = getenv("OWNER_ID", "5186954055")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Mus_3b")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ssstss")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ssstss")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5186954055").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
