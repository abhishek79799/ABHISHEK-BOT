from .. import BotzHub
from telethon import events, Button, client

SMEX_USER = [1528243010]

@BotzHub.on(
    events.NewMessage(pattern="^/add ?(.*)", func=lambda e: e.sender_id in SMEX_USER)
)
async def _(event):
  text = event.pattern_match.group(1)
  k = [[Button.text(text)]]
  await BotzHub.send_message(event.chat_id, f"Done added {text}")
  await event.reply("PERU HERE",
                    buttons=[
                        [Button.url("πΌπ’ πΎπ πππ", "t.me/Abhishek_xD")]
                    ])

    
@BotzHub.on(
    events.NewMessage(pattern="^/skem ?(.*)", func=lambda e: e.sender_id in SMEX_USER)
)
async def amdddd(event):
    text = event.pattern_match.group(1)
    k = [[Button.text(text)]]
    await BotzHub.send_message(event.chat_id, "π", buttons=k)
    
@BotzHub.on(events.NewMessage(pattern="^/skem"))
async def start_all(event):
    if event.is_private:
        await event.reply("vro use this cmd in group not in pm")
###################################################
@BotzHub.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "π·π΄ππ΄ πΈπ πΌπ πΌπ°πππ΄π πππ΄ππ½π°πΌπ΄  @Abhishek_xD")

########################################################################################################################################
