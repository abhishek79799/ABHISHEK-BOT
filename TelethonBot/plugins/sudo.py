from .. import BotzHub
import os

import heroku3
from telethon.tl.functions.users import GetFullUserRequest

from TelethonBot.config import Config, Var

Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USERS", None)


@BotzHub.on(pattern="sudo"))
async def sudo(event):
    sudo = "True" if Config.SUDO_USERS else "False"
    users = os.environ.get("SUDO_USERS", None)
    if sudo == "True":
        await eor(event, f"**Lion**\nSudo - `Enabled`\nSudo user(s) - `{users}`")
    else:
        await eor(event, f"**Lion**\nSudo - `Disabled`")


@BotzHub.on((pattern="prefix"))
async def handler(event):
    hndlr = Config.CMD_HNDLR
    if hndlr == r"\.":
        x = "."
    else:
        x = Config.CMD_HNDLR

    sudohndlr = Config.SUDO_HNDLR
    await eor(event, f"Command Handler - {x}\nSudo Handler - {sudohndlr}")


@BotzHub.on(admin_cmd(pattern="addsudo(?: |$)"))
async def tb(event):
    ok = await eor(event, "α∂∂ιηg υsεя αs sυ∂σ υsεя...")
    Lion = "SUDO_USERS"
    if Var.HEROKU_APP_NAME is not None:
        app = Heroku.app(Var.HEROKU_APP_NAME)
    else:
        await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
        return
    heroku_var = app.config()
    if event is None:
        return
    try:
        target = await get_user(event)
    except Exception:
        await ok.edit(f"Reply to a user.")
    if sudousers:
        newsudo = f"{sudousers} {target}"
    else:
        newsudo = f"{target}"
    await ok.edit(
        f"Aᴅᴅᴇᴅ `{target}` ᴀs ᴀ sᴜᴅᴏ ᴜsᴇʀ. ɴᴏᴡ ʀᴇsᴛᴀʀᴛɪɴɢ ʟɪᴏɴ X.. ɢɪᴍᴍᴇ sᴏᴍᴇ ᴍɪɴᴜᴛᴇs..."
    )
    heroku_var[Lion] = newsudo


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
