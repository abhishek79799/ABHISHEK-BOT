# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("𝙷𝙴𝙻𝙻𝙾 𝚅𝙼𝚁𝙾",
                    buttons=[
                        [Button.url("Moi Creator", url="https://t.me/shashank_xD")],
                        [Button.inline("Support Group", url="https://t.me/coffinxsupport")]
                    ])

@BotzHub.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")
