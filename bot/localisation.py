#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Nirusaki

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hi,<u>ANIKIDS</u> \n <b>Welcome To AniXcoder</b> \n <b>It Re-Encodes Videos With Latest Video And Audio Codecs Using </b> <u> FFMPEG </u>"
   
    ABS_TEXT = "Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "<b>📥 Trying To Downloading 📥</b> \n"
    
    UPLOAD_START = "<b>📤 Uploading 📤 </b> \n"
    
    COMPRESS_START = "<b>🍘 Starting To Encode 🍘</b>"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload ⬆️ files greater than 1.95GB due to Telegram API Limitations."
    
    COMPRESS_SUCCESS = "©️ @FIERCENETWORK"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "<b>Custom Thumbnail Saved</b>"
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "<b>✅ Custom Thumbnail Cleared Successfully.</b>"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "<b>✅ Downloaded Successfully.</b>"
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "<b>Hi, I Am AniXcoder Just Send Me Files And I Will Start Rencoding Them</b>"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
