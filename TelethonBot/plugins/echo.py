from .. import BotzHub
from telethon import TelegramClient, events


@client.on(events.NewMessage(incoming=True))
async def echo(event):
 echo = event.text
 await event.reply(echo)
 
client.run_until_disconnected()
