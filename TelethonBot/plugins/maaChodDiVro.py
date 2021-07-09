from .. import BotzHub
from telethon import events, Button, client

SMEX_USER = [1851709280, 1024855816, 1257356127]

@BotzHub.on(
    events.NewMessage(pattern="^/skem ?(.*)", func=lambda e: e.sender_id in SMEX_USER)
)
async def _(event):
  reply_message = await event.get_reply_message()
  k = [[Button.text(f"{reply_message}")]]
  k += [[custom.Inline.Button("🗑️ Delete msg", data="omkdel")]]
  await BotzHub.send_message(event.chat_id, "🤡", buttons=k)

@BotzHub.on(events.NewMessage(pattern="^/skem"))  # pylint: disable=oof
async def start_all(event):
    if not e.sender_id == SMEX_USER:
        await BotzHub.send_message(event.chat_id, "jana lwde gand mara")
