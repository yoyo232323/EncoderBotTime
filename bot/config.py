from bot.get_cfg import get_config
class Config(object):
    SESSION_NAME = get_config("SESSION_NAME", "AHCompressorBot")
    FFMPEG = get_config("FFMPEG")
    APP_ID = int(get_config("APP_ID", 12345))
    API_HASH = get_config("API_HASH", "")
    LOG_CHANNEL = get_config("LOG_CHANNEL")
    LOGZ = get_config("LOGZ")
    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None)
    AUTH_USERS = set(
        int(x) for x in get_config(
            "AUTH_USERS",
            should_prompt=True
        ).split()
    )
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "")
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "/app/downloads")
    BOT_USERNAME = get_config("BOT_USERNAME", "")
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    MAX_MESSAGE_LENGTH = 4096
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "■")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "□")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
