from telegram import Bot
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)

user=bot.get_me()
print(user.first_name)