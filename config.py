# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("25867809", "asura_bots")

API_HASH = os.environ.get("a9e21911e7c1a8bbfe74665afea65be8", "asura_bots")

BOT_TOKEN = os.environ.get("6446114677:AAGAahpIZ1oAZ7NuMGD8WBtNueIOUnMyi_I", "asura_bots") 

FORCE_SUB = os.environ.get("FORCE_SUB", "VJ_Botz") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("itzsuvo04", "renamevjbot")     

DB_URL = os.environ.get("mongodb+srv://itzsuvo04:)9U4zKwvSy7uEb%@cluster0.klrslpu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
