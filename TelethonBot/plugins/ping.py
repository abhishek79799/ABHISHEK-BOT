from .. import BotzHub
from telethon import events
import time import time
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

@BotzHub.on(events.NewMessage(pattern="/ping"))
async def ok(event):
    start = time()
    m_reply = await m.reply_text("...")
    delta_ping = time() - start
    await m_reply.edit_text(
        f"ＰＯＮＧ!!\n"
        f"🤖 𝙿𝙸𝙽𝙶: `{delta_ping * 1000:.3f} 𝚖𝚜`"
    )

