# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27317700")

API_HASH = os.environ.get("API_HASH", "de1077f45e29e6abebcd2b9dd196be1d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7270402673:AAG3v9Hvkjn6lMouTtFcCIxCuTd6RtS8wuk") 

FORCE_SUB = os.environ.get("FORCE_SUB", "notcrazyhuman") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "sayyed")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://sayyed:ks86@moviedownloder.zgrz9sz.mongod.net/retryWrites=true&w=majority&appName=MOVIEDOWNLODR")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5881638979').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
