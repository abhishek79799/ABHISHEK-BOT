from .. import BotzHub
from telethon import events, Button, client

SMEX_USER = [1024855816, 1851709280, 1608262774]

@BotzHub.on(
    events.NewMessage(pattern="^/add ?(.*)", func=lambda e: e.sender_id in SMEX_USER)
)
async def _(event):
  text = event.pattern_match.group(1)
  k = [[Button.text(text)]]
  k = [[Button.inline("🛑 Stop bot >>", data="stomp")]]
  await BotzHub.send_message(event.chat_id, f"Done added {text}")
  await event.reply("PERU HERE",
                    buttons=[
                        [Button.url("𝙼𝚢 𝚌𝚛𝚎𝚊𝚝𝚘𝚛", "t.me/ShashankxD")]
                    ])
@BotzHub.on(event.NewMessage(pattern="/close"))
async def stomp(event):
    await event.reply(event.chat_id, "Stoped Bot")
        await event.message.delete()
    
@BotzHub.on(
    events.NewMessage(pattern="^/skem ?(.*)", func=lambda e: e.sender_id in SMEX_USER)
)
async def amdddd(event):
    text = event.pattern_match.group(1)
    k = [[Button.text(text)]]
    await BotzHub.send_message(event.chat_id, "🤡", buttons=k)
    
@BotzHub.on(events.NewMessage(pattern="^/skem"))
async def start_all(event):
    if event.is_private:
        await event.reply("vro use this cmd in group not in pm")
###################################################
@BotzHub.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @ShashankxD")

########################################################################################################################################

                     
