# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, custom, Button
SMEX_PIC = "https://telegra.ph/file/1a50184a4c99440222c7e.jpg"
@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.send_file("ＨＥＬＬＯ  ＶＭＲＯ!!\n𝙸'𝙼 𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙾𝙵 @ShashankxD \n𝙿𝚁𝙴𝚂𝚂 𝚃𝙷𝙴 𝙱𝙴𝙻𝙾𝚆 𝙱𝚄𝚃𝚃𝙾𝙽 𝚃𝙾 𝙺𝙽𝙾𝚆 𝙼𝙾𝚁𝙴 𝙰𝙱𝙾𝚄𝚃 𝚂𝙷𝙰𝚂𝙷𝙰𝙽𝙺",
                    file=SMEX_PIC,
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
    await event.edit("HELP MENU",
                    buttons=[
                        [Button.inline("Master tool >>", data="ots")],
                        [Button.inline("tools", data="mhelp")]
                    ])
                     
@BotzHub.on(events.callbackquery.CallbackQuery(data="pkng"))
async def ommmmmmk(event):
    bamck = [[custom.Button.inline("BACK 🔙", data="baack")]]
    await event.edit("/skem to start smexing./n/stop to stop smex./n/ping to check bot ping./n/alive to check bot is alive or not./n/gcast to globally send message via bot", buttons=bamck)
    
@BotzHub.on(events.callbackquery.CallbackQuery(data="pkng"))
async def ooooopp(event):
    await event.edit("BHAJ YAAR TUM GAND MARAO")
