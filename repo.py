from telethon import events, Button

SMEX_USER = [1809900087]

@tbot.on(
    events.NewMessage(pattern="^/repo ?(.*)"))
async def _(event):
  if event.sender_id == SMEX_USER:
    await tbot.send_message(HEY MASTER HERE IS YOUR REPO\n\nhttps://github.com/R2K-VENOM/TelethonBot)
  else:
    await event.reply("**BHAI YAAR THUM GAAND MARAO**")
