from .. import BotzHub
from telethon import events, Button



@BotzHub.on(events.NewMessage(incoming=True, pattern="/smex"))
async def _(event):
 k = [[Button.text("/start"), Button.text("/start")]]
 k += [[Button.text("/start"), Button.text("/start")]]
 k += [[Button.text("/start"), Button.text("/start")]]
 k += [[Button.text("/start"), Button.text("/start")]]
 k += [[Button.text("/start"), Button.text("/start")]]
 k += [[Button.text("/start"), Button.text("/start")]]
 k += [[Button.text("/start"), Button.text("/start")]]
 k += [[Button.text("/start"), Button.text("/start")]]
 k += [[Button.text("/start"), Button.text("/start")]]
 for x in range(30):
  await bot.send_message(event.chat.id, "Hm", buttons=k)
