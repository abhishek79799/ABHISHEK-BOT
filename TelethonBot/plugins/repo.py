from telethon import events, Button

from . import *

SMEX_USER = [1809900087]

@bot.on(
    events.NewMessage(pattern="^/repo ?(.*)"))
async def _(event):
  if event.sender_id == SMEX_USER:
    await bot.send_message(HEY MASTER HERE IS YOUR REPO\n\nhttps://github.com/R2K-VENOM/TelethonBot)
  else:
    await event.reply("**BHAI YAAR THUM GAAND MARAO**")
