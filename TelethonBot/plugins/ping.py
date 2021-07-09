from telethon import events
import time
from datetime import datetime

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@BotzHub.on(events.NewMessage(pattern=None))
async def ok(event):
    msg = str(event.text)
    if not msg == "/ping":
     return

    start_time = datetime.datetime.now()
    message = await event.reply("[•] Ping [•]")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b><i>𝙿𝙾𝙽𝙶!!</i></b>\n"
        "<b>• 𝚃𝙸𝙼𝙴 𝚃𝙰𝙺𝙴𝙽:</b> <code>{}</code>\n"
        "<b>• 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚂𝙺𝙴𝙼 𝙵𝚁𝙾𝙼:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )

