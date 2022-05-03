import asyncio
import io
import logging
import os
import shutil
import sys
import time
import traceback

from bot import (
    BOT_START_TIME,
    LOGGER,
    LOG_FILE_ZZGEVC,
    MAX_MESSAGE_LENGTH,
    AUTH_USERS,
    data,
    pid_list,
    FFMPEG
)

from bot.commands import Command
from bot.localisation import Localisation
from bot.helper_funcs.display_progress import (
    TimeFormatter,
    humanbytes
)

async def exec_message_f(client, message):
  if message.from_user.id in AUTH_USERS:
    if True:
        DELAY_BETWEEN_EDITS = 0.3
        PROCESS_RUN_TIME = 100
        cmd = message.text.split(" ", maxsplit=1)[1]

        reply_to_id = message.message_id
        if message.reply_to_message:
            reply_to_id = message.reply_to_message.message_id

        start_time = time.time() + PROCESS_RUN_TIME
        process = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        e = stderr.decode()
        if not e:
            e = "No Error"
        o = stdout.decode()
        if not o:
            o = "No Output"
        else:
            _o = o.split("\n")
            o = "`\n".join(_o)
        OUTPUT = f"**QUERY:**\n__Command:__\n`{cmd}` \n__PID:__\n`{process.pid}`\n\n**stderr:** \n`{e}`\n**Output:**\n{o}"

        if len(OUTPUT) > MAX_MESSAGE_LENGTH:
            with open("exec.text", "w+", encoding="utf8") as out_file:
                out_file.write(str(OUTPUT))
            await client.send_document(
                chat_id=message.chat.id,
                document="exec.text",
                caption=cmd,
                disable_notification=True,
                reply_to_message_id=reply_to_id
            )
            os.remove("exec.text")
            await message.delete()
        else:
            await message.reply_text(OUTPUT)
  else:
    return
async def eval_message_f(client, message):
    if message.from_user.id in AUTH_USERS:
        status_message = await message.reply_text("Processing ...")
        cmd = message.text.split(" ", maxsplit=1)[1]

        reply_to_id = message.message_id
        if message.reply_to_message:
            reply_to_id = message.reply_to_message.message_id

        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None

        try:
            await aexec(cmd, client, message)
        except Exception:
            exc = traceback.format_exc()

        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr

        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Success"

        final_output = (
            "<b>EVAL</b>: <code>{}</code>\n\n<b>OUTPUT</b>:\n<code>{}</code> \n".format(
                cmd, evaluation.strip()
            )
        )

        if len(final_output) > MAX_MESSAGE_LENGTH:
            with open("eval.text", "w+", encoding="utf8") as out_file:
                out_file.write(str(final_output))
            await message.reply_document(
                document="eval.text",
                caption=cmd,
                disable_notification=True,
                reply_to_message_id=reply_to_id,
            )
            os.remove("eval.text")
            await status_message.delete()
        else:
            await status_message.edit(final_output)


async def aexec(code, client, message):
    exec(
        f"async def __aexec(client, message): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


async def upload_log_file(client, message):
  if message.from_user.id in AUTH_USERS:
    await message.reply_document(
        LOG_FILE_ZZGEVC
    )
  else:
    return

async def run_subprocess(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    return await process.communicate()

async def upload_dir(client, message):
  if message.from_user.id in AUTH_USERS:
    if True:
        cmd1 = message.text.split(" ", maxsplit=1)[1]
        print(cmd1)
        replyid = message.message_id
        if message.reply_to_message:
          replyid = message.reply_to_message.message_id
  if os.path.exists(cmd1):
    xhamster = await message.reply_text('Uploading The File 📁')
    await client.send_document(
                chat_id=message.chat.id,
                document=cmd1,
                caption=cmd1,
                reply_to_message_id=replyid,
        )
    await xhamster.delete_messages
  else:
     await message.reply_text(f"Directory Not Found ```{cmd1}```", parse_mode="markdown")
        
async def sample_gen(app, message):
  if message.chat.id not in AUTH_USERS:
     await message.reply_text("You Are Not Authorised To Use This Bot")
  if message.reply_to_message:
     vid = message.reply_to_message.message_id
     dp = await message.reply_to_message.reply_text("Downloading The Video", parse_mode="markdown")
     video = await app.download_media(
        message=message.reply_to_message,
        file_name='/app/samplevideo.mkv',
        )
     await dp.edit("Downloading Finished Starting To Generate Sample")
     video_file='/app/samplevideo.mkv'
     output_file='/app/sample_video.mkv'
     await dp.edit("Generating Sample...This May Take Few Moments")
     file_gen_cmd = f'ffmpeg -ss 00:30 -i "{video_file}" -t 30 "{output_file}" -y'
     output = await run_subprocess(file_gen_cmd)
  else:
     await message.reply_text('NO FILE DETECTED')
  if os.path.exists(output_file):
     await dp.edit('Uploading The Video')
     await app.send_document(
           chat_id=message.chat.id,
           document=output_file,
           caption="30 SECONDS SAMPLE",
           reply_to_message_id=message.reply_to_message,
     )
     await dp.delete()
     os.remove(video_file)
     os.remove(output_file)
  else:
     await dp.edit("Failed To Generate Sample Due To Locked Infrastructure")
     os.remove(video_file)
