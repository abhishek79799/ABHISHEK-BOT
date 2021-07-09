from .. import BotzHub
from telethon import events, Button, client

SMEX_USER = [1851709280, 1024855816, 1257356127]

@BotzHub.on(
    events.NewMessage(pattern="^/skem ?(.*)", func=lambda e: e.sender_id in SMEX_USER)
)
async def _(event):
  reply_message = await event.get_reply_message()
  k = [[Button.text(f"{reply_message}")]]
  await BotzHub.send_message(event.chat_id, "🤡", buttons=k)
  await event.reply("PERU HERE",
                    buttons=[
                        [Button.inline("𝙼𝚢 𝚌𝚛𝚎𝚊𝚝𝚘𝚛", data="Creator")]
                    ])

@BotzHub.on(events.NewMessage(pattern="^/skem"))  # pylint: disable=oof
async def start_all(event):
    if not event.sender_id == SMEX_USER:
        await BotzHub.send_message(event.chat_id, "jana lwde gand mara")
                    
###################################################
@BotzHub.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(_, CallBackQuery):
    await app.answer_callback_query(CallbackQuery.id, "𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @ShashankxD")

########################################################################################################################################

                     
