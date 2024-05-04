# Import libraries:
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile, Bot
from telegram.ext import ContextTypes, CallbackContext

# Import Configure:
from paths_config import *

# Constantes:
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)

## Candies:
async def candies(update: Update, context: ContextTypes):
    # Crear el menú de selección de imágenes de Dulces con THC
    keyboard = [[InlineKeyboardButton(f"Candy {i}", callback_data=f'candy{i}')] for i in range(1, 5)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Selecciona un tipo de Dulces con THC:", reply_markup=reply_markup)

### Select Candy:
async def handle_candy_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    candy_selected = query.data
    candy_image_path = None
    candy_name = None
    
    if candy_selected == 'candy1':
        candy_image_path = candy_images[0]
        candy_name = "Jolly rancher gummies🍬 \n10 gomitas de THC 600 mg. cada una \n$320.00"
    elif candy_selected == 'candy2':
        candy_image_path = candy_images[1]
        candy_name = "Lifesavers gummies🍬 \n10 gomitas 5 sabores diferentes THC 600 mg. \n$524.00"
    elif candy_selected == 'candy3':
        candy_image_path = candy_images[2]
        candy_name = "Znickerz bites 🥧 \nTrozos de chocolates THC 500 mg. \n$384.00"
    elif candy_selected == 'candy4':
        candy_image_path = candy_images[3]
        candy_name = "THC-snickers 🍫 \nBarra de chocolate THC 1000 mg. \n$560.00"

    if candy_image_path:
        with open(candy_image_path, 'rb') as image_file:
            await bot.send_photo(chat_id=query.message.chat_id, photo=InputFile(image_file), caption=candy_name)
    else:
        print('No se encontró la imagen del Dulce seleccionado')