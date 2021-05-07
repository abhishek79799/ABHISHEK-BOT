# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("ＨＥＬＬＯ  ＶＭＲＯ!",
                    buttons=[
                        [Button.url("My CREATOR", url="https://t.me/shaahank_xD")],
                        [Button.inline("Support Group", url="https://t.me/coffinxsupport")]
                    ])

@BotzHub.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")
