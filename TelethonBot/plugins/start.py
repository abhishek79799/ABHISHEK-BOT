# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("ＨＥＬＬＯ  ＶＭＲＯ!!\n𝙸'𝙼 𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙾𝙵 @ShashankxD \n𝙿𝚁𝙴𝚂𝚂 𝚃𝙷𝙴 𝙱𝙴𝙻𝙾𝚆 𝙱𝚄𝚃𝚃𝙾𝙽 𝚃𝙾 𝙺𝙽𝙾𝚆 𝙼𝙾𝚁𝙴 𝙰𝙱𝙾𝚄𝚃 𝚂𝙷𝙰𝚂𝙷𝙰𝙽𝙺",
                    buttons=[
                        [Button.inline("My creator", data="Creator")],
                        [Button.inline("HELP", data="mhelp")]
                    ])

@BotzHub.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @ShashankxD", show_alert=True)

########################################################################################################################################


@BotzHub.on(events.callbackquery.CallbackQuery(data="mhelp"))
async def ommmmk(event):
    but = [[custom.Button.inline("TOOLS »»", data="pkng")]]
    but += [[custom.Button.inline("OWNER TOOLS »»", data="ots")]]
    await event.edit("HELP MENU", button=but)
                     
@BotzHub.on(events.callbackquery.CallbackQuery(data="ots"))
async def ommmmmmk(event):
    bamk_but = [[custom.Button.inline("BACK 🔙", data="baack")]]
    await event.edit("/skem /n/stop/n/ping/n/alive/n/gcast", buttons=bamck)
    
@BotzHub.on(events.callbackquery.CallbackQuery(data="pkng"))
async def ooooopp(event):
    await event.edit("BHAJ YAAR TUM GAND MARAO")
