# Import libraries:
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile, Bot, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext

# Import Configure:
from paths_config import *

# Constantes:
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)


# Seleccionar la cantidad de gramos por vaper:
async def type_vaper(update: Update, context: CallbackContext):
        # Crear el menú de las dos opciones:
    keyboard = [
        [InlineKeyboardButton("Vapers 1 gramo", callback_data='vapers_1gm')],
        [InlineKeyboardButton("Vapers 2 gramos", callback_data='vapers_2gm')]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Selecciona la cantidad de gramos:", reply_markup=reply_markup)

## Vapers:
async def vapers(update: Update, context: ContextTypes):
    # Crear el menú de selección de imágenes de Vapers
    keyboard = [[InlineKeyboardButton(f"Vaper {i}", callback_data=f'vaper{i}')] for i in range(1, 11)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Selecciona un tipo de Vaper:", reply_markup=reply_markup)

### Select Vaper:
async def handle_vaper_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    vaper_selected = query.data
    vaper_image_path = None
    vaper_name = None
    
    if vaper_selected == 'vaper1':
        vaper_image_path = vaper_images[0]
        vaper_name = "Lonzo Cream 🍨⚡\nSativa\n1000 mg. de THC\n$1,200.00"
    elif vaper_selected == 'vaper2':
        vaper_image_path = vaper_images[1]
        vaper_name = "Cali Connected 🇨🇴🔥\nSativa\n1000 mg. de THC\n$1,200.00"
    elif vaper_selected == 'vaper3':
        vaper_image_path = vaper_images[2]
        vaper_name = "Tropical Gelato 🏝🍹\nIndica\n1000 mg. de THC\n$1,200.00"
    elif vaper_selected == 'vaper4':
        vaper_image_path = vaper_images[3]
        vaper_name = "Gold Coast Clear Premiun 🐻👑\nSativa\n1000 mg. de THC\n$1,200.00"
    elif vaper_selected == 'vaper5':
        vaper_image_path = vaper_images[4]
        vaper_name = "Dosi Killer 🐾\nSativa\n1000 mg. de THC\n$1,200.00"
        
    elif vaper_selected == 'vaper6':
        vaper_image_path = vaper_images[5]
        vaper_name = "Pack Man 💀\nSabor: Moras🍇\nIndica\n2000 mg. de THC\n$1,500.00"
    elif vaper_selected == 'vaper7':
        vaper_image_path = vaper_images[6]
        vaper_name = "Pack Man 💀\nSabor: Moras azules🫐\nSativa\n2000 mg. de THC\n$1,500.00"
    elif vaper_selected == 'vaper8':
        vaper_image_path = vaper_images[7]
        vaper_name = "Pack Man 💀\nSabor: Chicle🍬\nHíbrida\n2000 mg. de THC\n$1,500.00"
    elif vaper_selected == 'vaper9':
        vaper_image_path = vaper_images[8]
        vaper_name = "Pack Man 💀\nSabor: Durazno dulce🍑\nIndica\n2000 mg. de THC\n$1,500.00"
    elif vaper_selected == 'vaper10':
        vaper_image_path = vaper_images[9]
        vaper_name = "Pack Man 💀\nSabor: Piña agria🍍\nSativa\n2000 mg. de THC\n$1,500.00"
    elif vaper_selected == 'vaper11':
        vaper_image_path = vaper_images[10]
        vaper_name = "Vaper 11 XXXXXX $XXX.00"
    elif vaper_selected == 'vaper12':
        vaper_image_path = vaper_images[12]
    if vaper_image_path:
        with open(vaper_image_path, 'rb') as image_file:
            await bot.send_photo(chat_id=query.message.chat_id, photo=InputFile(image_file), caption=vaper_name)
    else:
        print('No se encontró la imagen del Vaper seleccionado')
