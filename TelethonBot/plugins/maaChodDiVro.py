from .. import BotzHub
from telethon import events, Button, client

SMEX_USER = [1851709280, 1024855816, 1257356127]

@BotzHub.on(
    events.NewMessage(pattern="^/skem ?(.*)", func=lambda e: e.sender_id in SMEX_USER)
)
async def _(event):
  k = [[Button.text(f"{event.message_text}")]]
  await BotzHub.send_message(event.chat_id, "🤡", buttons=k)
