#NIRUSAKI#
from datetime import datetime as dt
import os
from bot import (
    APP_ID,
    API_HASH,
    AUTH_USERS,
    DOWNLOAD_LOCATION,
    LOGGER,
    TG_BOT_TOKEN,
    BOT_USERNAME,
    SESSION_NAME,
    data,
    app
)
from bot.helper_funcs.utils import add_task, on_task_complete
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler

from bot.plugins.incoming_message_fn import (
    incoming_start_message_f,
    incoming_compress_message_f,
    incoming_cancel_message_f
)


from bot.plugins.status_message_fn import (
    eval_message_f,
    exec_message_f,
    upload_log_file
)

from bot.commands import Command
from bot.plugins.call_back_button_handler import button
sudo_users = "5121002601" 

uptime = dt.now()

def ts(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "")
        + ((str(hours) + "h, ") if hours else "")
        + ((str(minutes) + "m, ") if minutes else "")
        + ((str(seconds) + "s, ") if seconds else "")
        + ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]


if __name__ == "__main__" :
    
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
        
    app.set_parse_mode("html")
    incoming_start_message_handler = MessageHandler(
        incoming_start_message_f,
        filters=filters.command(["start", f"start@{BOT_USERNAME}"])
    )
    app.add_handler(incoming_start_message_handler)
    
            
    @app.on_message(filters.incoming & filters.command(["compress", f"compress@{BOT_USERNAME}"]))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("You Are Not Authorised To Use This Bot 🗑")
        query = await message.reply_text("Added to Queue ⏰...\nPlease Be Patient Encoding Will Start Soon", quote=True)
        data.append(message.reply_to_message)
        if len(data) == 1:
         await query.delete()   
         await add_task(message.reply_to_message)     
                                     
    @app.on_message(filters.incoming & filters.command(["restart", f"restart@{BOT_USERNAME}"]))
    async def restarter(app, message):
      await message.reply_text("Restarting The Bot Please Wait ⌚")
      quit(1)
        
    @app.on_message(filters.incoming & filters.command(["delthumb", f"delthumb@{BOT_USERNAME}"]))
    async def rmthumb(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("You Are Not Authorised To Use This Bot")
        if exists('/app/thumb.jpg'):
            os.system('rm thumb.jpg')
            await message.reply_text('Custom Thumbnail Removed 📸')
        else:
            await message.reply_text('No Custom Thumbnail Was Found 📸')
        
    @app.on_message(filters.incoming & filters.command(["clear", f"clear@{BOT_USERNAME}"]))
    async def restarter(app, message):
      data.clear()
      await message.reply_text("Successfully Cleared Queue...")
              
    @app.on_message(filters.incoming & (filters.video | filters.document))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("You Are Not Authorised To Use This Bot")
        query = await message.reply_text("Added to Queue ⏰...\nPlease Be Patient Encoding Will Start Soon", quote=True)
        data.append(message)
        if len(data) == 1:
         await query.delete()   
         await add_task(message)
            
    @app.on_message(filters.incoming & (filters.photo))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("You Are Not Authorised To Use This Bot 🗑")
        await message.download(file_name='/app/thumb.jpg')
        await message.reply_text('Thumbnail Added')
        
    @app.on_message(filters.incoming & filters.command(["cancel", f"cancel@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await incoming_cancel_message_f(app, message)

    @app.on_message(filters.incoming & filters.command(["eval", f"eval@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await eval_message_f(app, message)
        
    @app.on_message(filters.incoming & filters.command(["exec", f"exec@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await exec_message_f(app, message)
        
    @app.on_message(filters.incoming & filters.command(["stop", f"stop@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await on_task_complete()  
   
    @app.on_message(filters.incoming & filters.command(["help", f"help@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await message.reply_text("┏━━━━━━━━━━━━━━━━━\n┣✋ Hello I Am AniXcoder\n┣🧳Just Send Me Files And I Will Start Encoding\n┣📸I Will Automatically Generate Thumbnail\n┣🦾I Can Also Auto Rename\n┣🦾Created And Maintaine By\n┣@NIRUSAKI_MARVALE & @FIERCE_MARVALE\n┗━━━━━━━━━━━━━━━━━", quote=True)
        
    @app.on_message(filters.incoming & filters.command(["cmds", f"cmds@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await message.reply_text("┏━━━━━━━━━━━━━━━━━\n┣🚦Start - To The Start\n┣Cmds- To Repeat This List\n┣ Compress - To Compress The Video Manually\n┣Eval - Solve An Argument\n┣THUMB FEATURES COMING VERY SOON\n┣Clear - Clear The Queue\n┣Restart - Restart The Bot\n┗━━━━━━━━━━━━━━━━━", quote=True)
    
    @app.on_message(filters.incoming & filters.command(["log", f"log@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await upload_log_file(app, message)

    @app.on_message(filters.incoming & filters.command(["ping", f"ping@{BOT_USERNAME}"]))
    async def up(app, message):
      stt = dt.now()
      ed = dt.now()
      v = ts(int((ed - uptime).seconds) * 1000)
      ms = (ed - stt).microseconds / 1000
      p = f"🌋 PING = {ms}ms"
      await message.reply_text(v + "\n" + p)

    call_back_button_handler = CallbackQueryHandler(
        button
    )
    app.add_handler(call_back_button_handler)

    app.run()
