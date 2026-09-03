import re
from os import environ

# -------------------------
# Helper
# -------------------------
def str_to_bool(val, default=False):
    if val is None:
        return default
    return val.lower() in ("true", "1", "yes", "on")

# =========================================================
# 🤖 BOT BASIC INFORMATION
# =========================================================
API_ID = int(environ.get("API_ID", "31761013"))
API_HASH = environ.get("API_HASH", "3d55d62014467b2a922c6c0d6d95deae")
BOT_TOKEN = environ.get("BOT_TOKEN", "8875734725:AAFWujhaZqNQLKLw0sWm54LKeRcoLj8WcGU")
PORT = int(environ.get("PORT", "8080"))
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")
OWNER_USERNAME = environ.get("OWNER_USERNAME", "BlurpleOg")

# =========================================================
# 💾 DATABASE CONFIGURATION
# =========================================================
DB_URL = environ.get("DATABASE_URI", "mongodb+srv://dubbingroup29_db_user:itsyashjha@immortaldata.ojaeaxj.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DATABASE_NAME", "Yae_Probot")

# =========================================================
# 📢 CHANNELS & ADMINS
# =========================================================
ADMINS = int(environ.get("ADMINS", "7537243058"))

LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003982607035"))
PREMIUM_LOGS = int(environ.get("PREMIUM_LOGS", "-1003982607035"))
VERIFIED_LOG = int(environ.get("VERIFIED_LOG", "-1003982607035"))

POST_CHANNEL = int(environ.get("POST_CHANNEL", "-1003982607035"))
VIDEO_CHANNEL = int(environ.get("VIDEO_CHANNEL", "-1003916831742"))
BRAZZER_CHANNEL = int(environ.get("BRAZZER_CHANNEL", "-1003982607035"))

# Auth channels list
auth_channel_str = environ.get("AUTH_CHANNEL", "-1003982607035")
AUTH_CHANNEL = [int(x) for x in auth_channel_str.split() if x.strip().lstrip("-").isdigit()]

# =========================================================
# ⚙️ FEATURES & TOGGLES  (FIXED)
# =========================================================
FSUB = str_to_bool(environ.get("FSUB"), True)
IS_VERIFY = str_to_bool(environ.get("IS_VERIFY"), True)
POST_SHORTLINK = str_to_bool(environ.get("POST_SHORTLINK"), True)
SEND_POST = str_to_bool(environ.get("SEND_POST"), True)
PROTECT_CONTENT = str_to_bool(environ.get("PROTECT_CONTENT"), True)

# =========================================================
# 🔢 LIMITS
# =========================================================
DAILY_LIMIT = int(environ.get("DAILY_LIMIT", "5"))
VERIFICATION_DAILY_LIMIT = int(environ.get("VERIFICATION_DAILY_LIMIT", "20"))
PREMIUM_DAILY_LIMIT = int(environ.get("PREMIUM_DAILY_LIMIT", "50"))

# =========================================================
# 🔗 SHORTLINK & VERIFICATION
# =========================================================
SHORTLINK_URL = environ.get("SHORTLINK_URL", "vplink.in")
SHORTLINK_API = environ.get("SHORTLINK_API", "4a98bc00521b68207331e70bd5ebe380e8a855e8")
POST_SHORTLINK_URL = environ.get("POST_SHORTLINK_URL", "vplink.in")
POST_SHORTLINK_API = environ.get("POST_SHORTLINK_API", "4a98bc00521b68207331e70bd5ebe380e8a855e8")
VERIFY_EXPIRE = int(environ.get("VERIFY_EXPIRE", "3600"))
TUTORIAL_LINK = environ.get("TUTORIAL_LINK", "https://t.me/Tutorialfyy")

# =========================================================
# 💳 PAYMENT SETTINGS
# =========================================================
UPI_ID = environ.get("UPI_ID", "9838987214")
QR_CODE_IMAGE = environ.get("QR_CODE_IMAGE", "https://i.ibb.co/gZKRn65B/x.jpg")

# =========================================================
# 🖼️ IMAGES
# =========================================================
START_PIC = environ.get("START_PIC", "https://i.ibb.co/gZKRn65B/x.jpg")
AUTH_PICS = environ.get("AUTH_PICS", "https://i.ibb.co/gZKRn65B/x.jpg")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://i.ibb.co/gZKRn65B/x.jpg")
NO_IMG = environ.get("NO_IMG", "https://i.ibb.co/gZKRn65B/x.jpg")

# =========================================================
# 🌐 WEB APP
# =========================================================
WEB_APP_URL = environ.get("WEB_APP_URL", "https://t.me/LustyDormNeT")
