from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/alive"))
async def alibe(event):
  SMEX_PIC = "https://telegra.ph/file/3979593187378b2b54057.jpg"
  but = [[Button.url("Mʏ ᴍᴀsᴛᴇʀ »»", "t.me/R2K_VENOM")]]
  pm_caption = "•**I'M ALIVE AND READY TO SMEX**\n\n"
  pm_caption += "•**Mʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɢ**\n\n"
  pm_caption += "• Aʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ ✗\n\n"
  pm_caption += "• **𝙎𝙈𝙀𝙓 𝙓 𝙑𝙀𝙍𝙎𝙄𝙊𝙉**: `1.1`\n"
  pm_caption += "• **𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 𝙑𝙀𝙍𝙎𝙄𝙊𝙉** ☞ {version.__version__}\n"
  pm_caption += (
        "• **𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔** ☞ [𓆩𝙑𝙀𝙉𝙊𝙈𓆪](t.me/R2K_VENOM)\n\n"
    )
  pm_caption += f"• **𝘾𝙍𝙀𝘼𝙏𝙊𝙍** ☞ [𝚂𝙷𝙰𝚂𝙷𝙰𝙽𝙺](t.me/ShashankxD)\n"
  await BotzHub.send_file(event.chat_id, file=SMEX_PIC, captions=pm_caption, buttons=but, link_preview=False)
