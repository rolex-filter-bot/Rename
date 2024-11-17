# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28991562")

API_HASH = os.environ.get("API_HASH", "215d93eeacd3d1c704887f80b0b914f4")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7802188155:AAFr9B1YFLX_-7eu6PWHJM45PLTLMqyVwOM") 

FORCE_SUB = os.environ.get("FORCE_SUB", "TamillMobb_LinkkZz") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Cluster77")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://rlx10:rlx100@cluster77.mgtl0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster77")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/c6f79998e829fa0829eb1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6107997458').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
