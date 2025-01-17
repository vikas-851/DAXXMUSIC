import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "25064357"))
API_HASH = getenv("API_HASH", "cda9f1b3f9da4c0c93d1f5c23ccb19e2")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7262095494:AAFclA3a3SDbyFkedrnQcg5g2lZF87vTUI8")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","tanjiro1249")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Hinata_X_Music_robot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "˹Hɪɴᴀᴛᴀ ✘ Mᴜsɪᴄ˼ ❄️✨")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "hinatamusicassistant")
# ---------------------------------------------------------
UPSTREAM_REPO = UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/vikas-851/DAXXMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
) 
# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://tanjiro1564:tanjiro1564@cluster0.pp5yz4e.mongodb.net/?retryWrites=true&w=majority")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1001975521991))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7453770651))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

#-----------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+HbbYObIeHUw0NWQ1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+HbbYObIeHUw0NWQ1")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION1", "BAGDgkYAOoHYhWQAXAdpqp4SHfO66SLDVGarrGjxG660rDa5wflJ-V_zVlQRWFS3UJsHPfLAcHk_YskrW1LpLejOS_MZgzp9Jm7wTe-rc2aU8yOlCvUE7dUW6Bz5GkGpKMMaX55feHG2-4PWukY7P6XDmNPhTrfj8CyzrdbIbsUllHEDLhcT9dBAd_FohU0VZPj4q7dHpRI1KfKQ67oukIZCupgsTRgaiwx3wE2Ksah21_kifnbzmm6yWOq_Tk3uy5SB_qWS16xtH85xbBNHRBUTRCLnM8cXolTgoc67_FVb7RqNk9u9OcskZFi-tMF45Gpwz9jzTR6fpwGwZAAdhvOPv4ddGgAAAAG6HIryAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph//file/919714d04904fae43ffd0.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph//file/466d670a36728a36283c9.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/f4395ca92239d6de6df8b.jpg"
STATS_IMG_URL = "https://telegra.ph/file/a44534c784f1eac464d85.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/d03b8bbec0af13849e031.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/5767b8e5619d616c7bf71.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d83a2cf2bd0dd868f37ae.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/f4395ca92239d6de6df8b.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/35b034fe2cdc2effdd02e.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/45abf960687cff85f5855.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/eeff283b0ad70d40b80da.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/abdbf823aa2485c241b19.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
