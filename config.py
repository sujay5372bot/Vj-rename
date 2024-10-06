# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24935727")

API_HASH = os.environ.get("API_HASH", "3fd33336629324ecd664e9b6894f0909")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7554683184:AAFCmbIf9seBQrZoFcHwujmHbNfLP-rAm9M") 

FORCE_SUB = os.environ.get("FORCE_SUB", "https://t.me/sujay8371") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "sujay5372192")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://sujay5372192:sujay5372192@cluster00001.zivqq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster00001")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
