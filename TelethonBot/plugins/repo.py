from .. import BotzHub
from telethon import events, Button

SMEX_USER = [1769615810]

@BotzHub.on(events.NewMessage(pattern="^/repo ?(.*)"))
async def _(event):
  if event.sender_id in SMEX_USER:
    await BotzHub.send_message("**HEY MASTER HERE IS YOUR REPO**\n\nhttps://github.com/R2K-VENOM/TelethonBot")
  else:
    await event.reply("**BHAI YAAR THUM GAAND MARAO**")
