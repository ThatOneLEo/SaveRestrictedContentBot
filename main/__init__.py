#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28361668
API_HASH = "50b661fce21cd08a19d36a9761263d8b"
BOT_TOKEN = "6791474892:AAHBSjRMz-HT-nbEY1vU0YgOh_2GH5-cnMs"
SESSION = "BACr70_y1MRKfaRqnUWmoTcjj2EQWdUWk-GHQz737uIgH0hRroSPdrgM577uaFuPJscIEgbMGh8qQqoZQulmY8uwZ38omvfmiSuYKKDHx8shZds68gORNXN9ykFhyKoApSGbVoY2rOWl1iqAUKa9tUsNihU423LOYL4OmFzWLnDP8f_XHKd4JbATw8Z9YOha37k8CqEbGpiUyplS-m5xdKryfihhYJSUXF9qo-BJehgDBzbRFhcqJhxjAALSCq4JdPIMYf_vZMwbxvnf7lm-p7f_a3HqmPm-YT6Z5zt84V7ToYJwStMXl5ImO9F6-JemI-wAerX3TUHhQ-wUMOEZaAfBAAAAAXqT6EwA"
FORCESUB = "DroneBots"
AUTH = 6351480908

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
