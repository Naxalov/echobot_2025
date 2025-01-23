from telegram.ext import Updater,MessageHandler,Filters,CommandHandler,CallbackContext
from telegram import Bot, Update,InlineKeyboardButton,InlineKeyboardMarkup
import os



def echo(update: Update, context: CallbackContext):
    # Get text from update
    text = update.message.text
    # Check type of message
    if update.message.photo:
        # Send photo back
        update.message.reply_text("Photo")
    if update.message.sticker:
        # Send sticker back
        update.message.reply_text("Sticker")
    # Send text back
    update.message.reply_text(text)

def info(update: Update, context):
    inline_button = InlineKeyboardButton(text="Click me",callback_data=1)
    inline_keyboard = InlineKeyboardMarkup([[inline_button,inline_button]])
    update.message.reply_text("Hello, This is a bot just for tutorial",reply_markup=inline_keyboard)

def start(update: Update, context):
    update.message.reply_text("Hello, This is a bot just for tutorial")

TOKEN = os.getenv("TOKEN")

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

# add handlers here

dispatcher.add_handler(MessageHandler(filters=Filters.text('Hello'),callback=echo))

dispatcher.add_handler(CommandHandler('info',info))

dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()
