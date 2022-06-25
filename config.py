## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME    =    getenv ( " SESSION_NAME" , "AQAyE9nfCXEs4FrHShvon2xpWKO9flA36JOlEyqcs9OL3SU_HVQD3PWkRoZpaRjBUPYL5w9Li-tNjs2KVfSmcOw3D1utRJMvYaEeLcies9IZKpM7VjiHLb3jUOJZJg479BN48tSkY68nodw9kPUYl7c7xhCpsN6CDjFBs0KKR5yjqJiwHd0UnKN0BeLDc09h_6h7fq82zJpZq6Tk3XHYiN0OBQVRIcuF0P42WEIjvhdKH2Ddr3oVhihdpD93Fj4ZxxAxQURFzQweToCu_kOr00szJlkWjGz5TRkBOjika53_wL7btzzOkr1yQB0yWmb9W4BzMG9jQiF_LF7HxumACJMOAAAAAU1Ja6kA" )
BOT_TOKEN      =      getenv ( "BOT_TOKEN"     ،     "5538104001:AAGfwwlXgUrXT7nXZsV5RmzOmY-vsoolsXQ"   )
BOT_NAME = getenv("BOT_NAME", "𝖥𝗅𝗈𝖱𝖾𝖷")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Aken")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ssstss")
ALIVE_NAME = getenv("ALIVE_NAME", "Aken")
BOT_USERNAME  =  getenv ( "BOT_USERNAME" ، "ssTss_Bot" )
OWNER_ID = getenv("OWNER_ID", "5186954055")
ASSISTANT_NAME   =   getenv ( "ASSISTANT_NAME"  ،  "ssTss6" )
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
