# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26107882")

API_HASH = os.environ.get("API_HASH", "c6e1a5ec353a580428bf7e6743fc7f46")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6388930165:AAEGNOTlkyhPtQhuUgiUfk9UzvoFdq0WXaY") 

FORCE_SUB = os.environ.get("FORCE_SUB", "heresthemovies4") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "arthguptacms")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://arthguptacms:3qV67VHCnF2zJIma@cluster0.cxp12.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2104240939').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
