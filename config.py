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
CMD_MSG = "⚙️ 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖠𝖽𝗆𝗂𝗇! 𝖧𝖾𝗋𝖾'𝗌 𝗒𝗈𝗎𝗋 𝖼𝗈𝗇𝗍𝗋𝗈𝗅 𝗉𝖺𝗇𝖾𝗅. \n\n/addch — 𝖠𝖽𝖽 𝖺 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗍𝗁𝖾 𝖻𝗈𝗍 (𝖺𝖽𝗆𝗂𝗇 𝗈𝗇𝗅𝗒) \n\n/delch — 𝖱𝖾𝗆𝗈𝗏𝖾 𝖺 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝖻𝗈𝗍 (𝖺𝖽𝗆𝗂𝗇 𝗈𝗇𝗅𝗒) \n\n/channels — 𝖲𝗁𝗈𝗐 𝖺𝗅𝗅 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝖾𝖽 𝖼𝗁𝖺𝗇𝗇𝖾𝗅𝗌 \n\n/reqlink — 𝖲𝗁𝗈𝗐 𝖺𝗅𝗅 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 𝗅𝗂𝗇𝗄𝗌 𝖿𝗈𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅𝗌 (𝗉𝖺𝗀𝗂𝗇𝖺𝗍𝖾𝖽) \n\n/links — 𝖲𝗁𝗈𝗐 𝖺𝗅𝗅 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗅𝗂𝗇𝗄𝗌 𝖺𝗌 𝗍𝖾𝗑𝗍 (𝗉𝖺𝗀𝗂𝗇𝖺𝗍𝖾𝖽) \n\n/bulklink — 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗅𝗂𝗇𝗄𝗌 𝖿𝗈𝗋 𝗆𝗎𝗅𝗍𝗂𝗉𝗅𝖾 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝖨𝖣𝗌 𝖺𝗍 𝗈𝗇𝖼𝖾 \n\n/genlink — 𝖲𝗍𝗈𝗋𝖾 𝖺𝗇𝖽 𝖾𝗇𝖼𝗈𝖽𝖾 𝖺𝗇𝗒 𝖾𝗑𝗍𝖾𝗋𝗇𝖺𝗅 𝗅𝗂𝗇𝗄, 𝗀𝖾𝗍 𝖺 𝗍.𝗆𝖾 𝗌𝗍𝖺𝗋𝗍 𝗅𝗂𝗇𝗄 𝖿𝗈𝗋 𝗂𝗍 \n\n/channels — 𝖲𝗁𝗈𝗐 𝖺𝗅𝗅 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝖾𝖽 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝖨𝖣𝗌 𝖺𝗇𝖽 𝗇𝖺𝗆𝖾𝗌 \n\n/reqtime — 𝖲𝖾𝗍 𝗍𝗁𝖾 𝖺𝗎𝗍𝗈-𝖺𝗉𝗉𝗋𝗈𝗏𝖾 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 𝗍𝗂𝗆𝖾𝗋 𝖽𝗎𝗋𝖺𝗍𝗂𝗈𝗇. \n\n/reqmode — 𝖳𝗈𝗀𝗀𝗅𝖾 𝖺𝗎𝗍𝗈 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 𝖺𝗉𝗉𝗋𝗈𝗏𝖺𝗅 𝗆𝗈𝖽𝖾 (𝖮𝖭/𝖮𝖥𝖥). \n\n/approveon — 𝖤𝗇𝖺𝖻𝗅𝖾 𝖺𝗎𝗍𝗈 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 𝖺𝗉𝗉𝗋𝗈𝗏𝖺𝗅 𝖿𝗈𝗋 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖼𝗁𝖺𝗇𝗇𝖾𝗅. \n\n/approveoff — 𝖣𝗂𝗌𝖺𝖻𝗅𝖾 𝖺𝗎𝗍𝗈 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 𝖺𝗉𝗉𝗋𝗈𝗏𝖺𝗅 𝖿𝗈𝗋 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖼𝗁𝖺𝗇𝗇𝖾𝗅. \n\n/approveall— 𝖠𝗉𝗉𝗋𝗈𝗏𝖾 𝖺𝗅𝗅 𝗉𝖾𝗇𝖽𝗂𝗇𝗀 𝗃𝗈𝗂𝗇 𝗋𝖾𝗊𝗎𝖾𝗌𝗍𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗎𝗌𝗂𝗇𝗀 𝗎𝗌𝖾𝗋𝖻𝗈𝗍 (𝗆𝖺𝗄𝖾 𝗌𝗎𝗋𝖾 𝗍𝗈 𝖿𝗂𝗅𝗅 𝗒𝗈𝗎𝗋 𝗌𝖾𝗌𝗌𝗂𝗈𝗇 𝗌𝗍𝗋𝗂𝗇𝗀 𝗂𝗇 𝖺𝗉𝗉𝗋𝗈𝗏𝖾.𝗉𝗒). \n\nᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅ𝗌 \n\n/stats — 𝖲𝗁𝗈𝗐 𝖻𝗈𝗍 𝗌𝗍𝖺𝗍𝗌 (𝗈𝗐𝗇𝖾𝗋 𝗈𝗇𝗅𝗒) \n/status — 𝖲𝗁𝗈𝗐 𝖻𝗈𝗍 𝗌𝗍𝖺𝗍𝗎𝗌 (𝖺𝖽𝗆𝗂𝗇𝗌) \n/broadcast — 𝖡𝗋𝗈𝖺𝖽𝖼𝖺𝗌𝗍 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝖺𝗅𝗅 𝗎𝗌𝖾𝗋𝗌"
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
