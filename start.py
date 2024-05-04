from telegram import Update, InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

## Crear menú de bienvenida:
async def start(update: Update, context: ContextTypes):
    # Crear los botones
    keyboard = [
        [InlineKeyboardButton("Vapers", callback_data='vapers')],
        [InlineKeyboardButton("Dulces con THC", callback_data='candies')],
        [InlineKeyboardButton("Cultivos", callback_data='weed')],
        [InlineKeyboardButton("Ayuda", callback_data='help')]
    ]
    # Adjuntar los botones al mensaje de bienvenida
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Hola, soy un King. ¿En qué puedo ayudarte?\nElige una opción:", reply_markup=reply_markup)
