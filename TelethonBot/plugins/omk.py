from .. import BotzHub
from telethon import event

@BotzHub.on(events.NewMessage(pattern="/skip"))
async def oommkkj(event):
  await event.send(event.chat_id, "**jana lwde**")
