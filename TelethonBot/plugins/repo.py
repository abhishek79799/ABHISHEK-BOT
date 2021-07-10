from .. import BotzHub
from telethon import events, Button

SMEX_USER = [1809900087]

@BotzHub.on(
    events.NewMessage(pattern="^/repo ?(.*)", func=lambda e: e.sender_id in SMEX_USER)
async def _(event):
    await BotzHub.send_message(HEY MASTER HERE IS YOUR REPO\n\nhttps://github.com/R2K-VENOM/TelethonBot)
  else:
    await event.reply("**BHAI YAAR THUM GAAND MARAO**")
