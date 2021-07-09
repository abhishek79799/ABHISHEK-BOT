from telethon import events, button
import time
from datetime import datetime

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def _omk(event):
  await event.reply("Click on below button to check ping",
                    buttons=[
                        [Button.inline("𝙿𝙸𝙽𝙶 >>",data="piing")]
                    ])

@BotzHub.on(events.callbackquery.CallbackQuery(data="piing"))
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds
    reply_pop_up_alert = f"💡 𝙱𝙾𝚃•𝙿𝙸𝙽𝙶 = {ms} 𝙼𝚂"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
