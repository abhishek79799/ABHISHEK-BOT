import os
from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))

class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    TOKEN = os.environ.get("TOKEN", None)
    SUDO_USERS = set(
        int(x) for x in os.environ.get(
            "SUDO_USERS",
            "1837687523").split())
    #Cumstom vamrs 
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
