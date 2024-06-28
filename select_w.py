# Import libraries:
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile, Bot
from telegram.ext import ContextTypes, CallbackContext

# Import Configure:
from paths_config import *
from start import start
# Constantes:
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)

## Weed:
async def weed(update: Update, context: ContextTypes):
    # Crear el menú de selección de imágenes de cultivos.
    keyboard = [
        [InlineKeyboardButton("Gelato👾", callback_data='weed1')],
        [InlineKeyboardButton("Gorilla🦍", callback_data='weed2')],
        [InlineKeyboardButton("Ethos Cookies 🍪", callback_data='weed3')],
        [InlineKeyboardButton("Alien Mintz👽", callback_data='weed4')],
        [InlineKeyboardButton("Candy Gas 🃏🍭", callback_data='weed5')],
        [InlineKeyboardButton("Volver al menú principal 🔙", callback_data='main_menu')],
        [InlineKeyboardButton("CERRAR ❌", callback_data='close')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    m = "<code>Menú de Cultivos 🌱</code>"+"\n"+"<b>Selecciona un botón:</b>"

    if update.message:
        await update.message.reply_text(m, reply_markup=reply_markup, parse_mode='html')
    elif update.callback_query and update.callback_query.message.text:
        await update.callback_query.message.edit_text(m, reply_markup=reply_markup, parse_mode='html')
    else:
        await context.bot.send_message(update.effective_chat.id, m, reply_markup=reply_markup, parse_mode='html')

### Select Weed:
async def handle_weed_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    weed_selected = query.data
    weed_image_path = None
    weed_name = None
    back_callback = 'weed'

    if weed_selected == 'close':
        await context.bot.delete_message(query.message.chat_id, query.message.message_id)
    elif weed_selected == 'main_menu':
        await start(query, context)
    else:
        if query.message.text:  # Verificar que el mensaje tenga contenido de texto
            await context.bot.delete_message(query.message.chat_id, query.message.message_id)
        if weed_selected == 'weed1':
            weed_image_path = weed_images[0]
            weed_name = "Gelato 👾 $800.00 Oz. \nPromo 2 onzas Por $1,200.00 🔥 \nMedia onza $350.00 🎭"
        elif weed_selected == 'weed2':
            weed_image_path = weed_images[1]
            weed_name = "Gorilla 🦍 $500.00 Oz. \nPromo 2 onzas Por $800.00 🔥 \nMedia onza $300 🎭"
        elif weed_selected == 'weed3':
            weed_image_path = weed_images[2]
            weed_name = "Ethos Cookies 🍪 $600.00 Oz. \nPromo 2 onzas Por $1,000.00 🔥 \nMedia onza $350 🎭"
        elif weed_selected == 'weed4':
            weed_image_path = weed_images[3]
            weed_name = "Alien Mintz 👽💸 $2,200.00 Oz. \nPromo 2 onzas Por $3,900.00 🔥🔥 \nMedia onza $1,200.00 🎭"
        elif weed_selected == 'weed5':
            weed_image_path = weed_images[4]
            weed_name = "Candy Gas 🃏🍭 $1,200.00 Oz. \nPromo 2 onzas Por $2,000.00 🔥 \nMedia onza $650.00 🎭"

        if weed_image_path:
            keyboard_back = [
                [InlineKeyboardButton("Volver al menú anterior 🔙", callback_data=back_callback)],
                [InlineKeyboardButton("Volver al menú principal 🔙", callback_data='main_menu')],
                [InlineKeyboardButton("CERRAR ❌", callback_data='close')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard_back)
            with open(weed_image_path, 'rb') as image_file:
                await bot.send_photo(chat_id=query.message.chat_id, photo=InputFile(image_file), caption=weed_name, reply_markup=reply_markup)
        else:
            print('No se encontró la imagen del Cultivo de Weed seleccionado')
