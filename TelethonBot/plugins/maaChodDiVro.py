from .. import BotzHub
from telethon import events, Button, client

SMEX_USER = [1851709280, 1024855816]

@BotzHub.on(
    events.NewMessage(pattern="^/skemm ?(.*)", func=lambda e: e.sender_id in SMEX_USER)
)
async def _(event):
  k = [[Button.text("comrade randi vai")]]
  await event.send_message(-1001158444924, "🌝", buttons=k)
