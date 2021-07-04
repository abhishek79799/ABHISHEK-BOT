from .. import BotzHub
from telethon import events, Button



@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def _(event):
 k = [[Button.text("comrade vro"), Button.text("Comrade vro")]]
 for x in range(30):
  await bot.send_message(-1001415644857, "🌝", buttons=k)
