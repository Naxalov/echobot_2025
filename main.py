from telegram import Bot
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)

user=bot.get_me()
update = bot.get_updates()[0]
message = update.message
print(message.text)



