from .. import BotzHub
from telethon import events, Button

SMEX_USER = 1851709280

@BotzHub.on(
    events.NewMessage(pattern="^/skem ?(.*)", func=lambda e: e.sender_id == SMEX_USER)
)
async def _(event):
 k = [[Button.text("comrade randi vai")]]
 for x in range(30):
  await bot.send_message(-1001599075750, "🌝", buttons=k)
    else:
        await event.send_message("jana bsdk gand mara")
