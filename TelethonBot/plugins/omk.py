from .. import BotzHub
from telethon import events

@BotzHub.on(events.NewMessage(pattern="/skip"))
async def oommkkj(event):
  await event.send(event.chat_id, "**jana lwde**")
