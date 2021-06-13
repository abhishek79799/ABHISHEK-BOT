# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("ＨＥＬＬＯ  ＶＭＲＯ!!\n𝙸'𝙼 𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙾𝙵 @ShashankxD \n𝙿𝚁𝙴𝚂𝚂 𝚃𝙷𝙴 𝙱𝙴𝙻𝙾𝚆 𝙱𝚄𝚃𝚃𝙾𝙽 𝚃𝙾 𝙺𝙽𝙾𝚆 𝙼𝙾𝚁𝙴 𝙰𝙱𝙾𝚄𝚃 𝚂𝙷𝙰𝚂𝙷𝙰𝙽𝙺",
                    buttons=[
                        [Button.inline("𝙼𝚢 𝚌𝚛𝚎𝚊𝚝𝚘𝚛", data="Creator")],
                        [Button.inline("𝚃𝙴𝙰𝙼 𝙲𝙾𝙵𝙵𝙸𝙽", data="TeamCoffin")]
                    ])

@BotzHub.on(events.callbackquery.CallbackQuery(data="Creator"))
async def ex(event):
    await event.edit("𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 = ShashankxD", show_alert=True)
  
########################################################################################################################################

@BotzHub.on(events.callbackquery.CallbackQuery(data="TeamCoffin"))
async def ex(event):
    await event.edit("𝙷𝙴𝚈!!\n𝚃𝙷𝙸𝚂 𝙸𝚂 𝚃𝙴𝙰𝙼 𝙲𝙾𝙵𝙵𝙸𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝚃\n𝙸𝙵 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙰𝙽𝚈 𝚀𝚄𝙴𝚂𝚃𝙸𝙾𝙽\n𝚈𝙾𝚄 𝙲𝙰𝙽 𝙰𝚂𝙺 𝚃𝙾 𝙾𝚄𝚁 𝙰𝙳𝙼𝙸𝙽𝚂\n\n© 𝚃𝙴𝙰𝙼 𝙲𝙾𝙵𝙵𝙸𝙽 𝚇")

                     
