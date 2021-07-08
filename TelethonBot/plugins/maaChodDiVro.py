from xDShashank.smex import SMEX_USER
from .. import BotzHub
from telethon import events, Button, client

SMEX_USER = [1851709280, 1024855816]
OMK_BUT = "paradise rand"
STIMCKER = "CAACAgUAAxkBAAEKscVg4s7cLSlvdXiZ-XUmM6Nmda5tygACDAQAApp9kFSQcgrtjd-dPCAE"
@BotzHub.on(
    events.NewMessage(pattern="^/skemm ?(.*)", func=lambda e: e.sender_id in SMEX_USER)
)
async def _(event):
  k = [[Button.text(f"{OMK_BUT}")]]
  await event.send_sticker(event.chat_id, STIMCKER, buttons=k)
