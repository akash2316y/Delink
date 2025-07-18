import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7880711027:AAF6mJAHEhwAdQEz_3qB5T_rtHqMx9ndADI")
APP_ID = int(os.environ.get("APP_ID", "21184495"))
API_HASH = os.environ.get("API_HASH", "7238819d51a5280143fc3023a2f1abed")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "8162859297"))
PORT = os.environ.get("PORT", "8022")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://akashrabha2005:781120@cluster0.pv6yd2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "link")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @Codeflix_Bots</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Messages
START_MSG = os.environ.get("START_MESSAGE", "𝖧𝖾𝗒 {mention}\n     𝖨 𝖺𝗆 𝖩𝗎𝗌𝗍 𝖺 𝗅𝗂𝗇𝗄 𝗌𝗁𝖺𝗋𝗂𝗇𝗀 𝖻𝗈𝗍.\n 𝖶𝗈𝗋𝗄𝗂𝗇𝗀 𝖥𝗈𝗋 𝖠𝗇𝗂𝗆𝖾 𝖬𝗎𝗌𝖾𝗎𝗆")
ABOUT_TXT = """𝖬𝖺𝖽𝖾 𝖡𝗒 : 𝖠𝗇𝗂𝗆𝖾 𝖬𝗎𝗌𝖾𝗎𝗆"""
CMD_MSG = "<b>⚙️ Welcome Admin! Here's your control panel.</b>"
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002849512654")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "8162859297").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(8162859297)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
