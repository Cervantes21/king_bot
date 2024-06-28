# # Import libraries:
# import os
# from dotenv import load_dotenv
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile, Bot
# from telegram.ext import CallbackContext

# # Import Configure:
# from paths_config import *
# from start import start
# # Constants:
# load_dotenv()
# token = os.getenv('TOKEN')
# bot = Bot(token=token)

# async def selected_vaper(update: Update, context: CallbackContext):
#     keyboard = [
#         [InlineKeyboardButton("🗡Vapers 1 gramo", callback_data='vapers_1g')],
#         [InlineKeyboardButton("⚔Vapers 2 gramos", callback_data='vapers_2g')],
#         [InlineKeyboardButton("Volver al menú principal 🔙", callback_data='main_menu')],
#         [InlineKeyboardButton("CERRAR ❌", callback_data='close')]
#     ]
#     markup = InlineKeyboardMarkup(keyboard)
#     m = '<b>Elige la cantidad de gramos:</b>'
#     if update.message:
#         await update.message.reply_text(m, reply_markup=markup, parse_mode='html')
#     elif update.callback_query:
#         await update.callback_query.message.edit_text(m, reply_markup=markup, parse_mode='html')

# async def vapers_1g(update: Update, context: CallbackContext):
#     keyboard_1g = [
#         [InlineKeyboardButton("Lonzo Cream🍨", callback_data='vaper1')],
#         [InlineKeyboardButton("Cali Connected🇨🇴🔥", callback_data='vaper2')],
#         [InlineKeyboardButton("Gold Coast Clear Premiun🐻", callback_data='vaper3')],
#         [InlineKeyboardButton("Tropical Gelato🍹", callback_data='vaper4')],
#         [InlineKeyboardButton("Dosi Killer💀", callback_data='vaper5')],
#         [InlineKeyboardButton("CERRAR ❌", callback_data='close')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard_1g)
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="Selecciona un botón para ver el Vaper:", reply_markup=reply_markup)

# async def vapers_2g(update: Update, context: CallbackContext):
#     keyboard_2g = [
#         [InlineKeyboardButton("☠Packman: Moras🍇", callback_data='vaper6')],
#         [InlineKeyboardButton("☠Packman: Moras azules🫐", callback_data='vaper7')],
#         [InlineKeyboardButton("☠Packman: Chicle🍬", callback_data='vaper8')],
#         [InlineKeyboardButton("☠Packman: Durazno🍑", callback_data='vaper9')],
#         [InlineKeyboardButton("☠Packman: Piña🍍", callback_data='vaper10')],
#         [InlineKeyboardButton("👾Backpack Boyz: Cereza🍒", callback_data='vaper11')],
#         [InlineKeyboardButton("👾Backpack Boyz: Limón-cereza🍋🍒", callback_data='vaper12')],
#         [InlineKeyboardButton("CERRAR ❌", callback_data='close')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard_2g)
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id, 
#         text="Selecciona un botón para ver el Vaper:", 
#         reply_markup=reply_markup,
#         parse_mode = 'HTML'
#     )

# async def send_vaper(update: Update, context: CallbackContext):
#     query = update.callback_query
#     vaper_selected = query.data
#     vaper_image_path = None
#     vaper_name = None
    
#     if vaper_selected == 'close':
#         context.bot.delete_message(query.message.chat_id, query.message.message_id)
#     elif vaper_selected == 'vaper1':
#         vaper_image_path = vaper_images[0]
#         vaper_name = "Lonzo Cream 🍨⚡\nSativa\n1000 mg. de THC\n$1,200.00"
#     elif vaper_selected == 'vaper2':
#         vaper_image_path = vaper_images[1]
#         vaper_name = "Cali Connected 🇨🇴🔥\nSativa\n1000 mg. de THC\n$1,200.00"
#     elif vaper_selected == 'vaper3':
#         vaper_image_path = vaper_images[2]
#         vaper_name = "Gold Coast Clear Premiun 🐻👑\nIndica\n1000 mg. de THC\n$1,200.00"
#     elif vaper_selected == 'vaper4':
#         vaper_image_path = vaper_images[3]
#         vaper_name = "Tropical Gelato 🏝🍹\nSativa\n1000 mg. de THC\n$1,200.00"
#     elif vaper_selected == 'vaper5':
#         vaper_image_path = vaper_images[4]
#         vaper_name = "Dosi Killer 🐾\nSativa\n1000 mg. de THC\n$1,200.00"
#     elif vaper_selected == 'vaper6':
#         vaper_image_path = vaper_images2m[0]
#         vaper_name = "Pack Man 💀\nSabor: Moras🍇\nIndica\n2000 mg. de THC\n$1,500.00"
#     elif vaper_selected == 'vaper7':
#         vaper_image_path = vaper_images2m[1]
#         vaper_name = "Pack Man 💀\nSabor: Moras azules🫐\nSativa\n2000 mg. de THC\n$1,500.00"
#     elif vaper_selected == 'vaper8':
#         vaper_image_path = vaper_images2m[2]
#         vaper_name = "Pack Man 💀\nSabor: Chicle🍬\nHíbrida\n2000 mg. de THC\n$1,500.00"
#     elif vaper_selected == 'vaper9':
#         vaper_image_path = vaper_images2m[3]
#         vaper_name = "Pack Man 💀\nSabor: Durazno dulce🍑\nIndica\n2000 mg. de THC\n$1,500.00"
#     elif vaper_selected == 'vaper10':
#         vaper_image_path = vaper_images2m[4]
#         vaper_name = "Pack Man 💀\nSabor: Piña agria🍍\nSativa\n2000 mg. de THC\n$1,500.00"
#     elif vaper_selected == 'vaper11':
#         vaper_image_path = vaper_images2m[5]
#         vaper_name = "Backpack Boyz 👾🎒\nSabor: Cereza🍒\nDiamantes Líquidos\n2000 mg. de THC\n$1,500.00"
#     elif vaper_selected == 'vaper12':
#         vaper_image_path = vaper_images2m[6]
#         vaper_name = "Pack Man 👾🎒\nSabor: Limón-cereza 🍒🍋\nDiamantes Líquidos\n2000 mg. de THC\n$1,500.00"

#     if vaper_image_path:
#         with open(vaper_image_path, 'rb') as image_file:
#             await context.bot.send_photo(chat_id=query.message.chat_id, photo=InputFile(image_file), caption=vaper_name)
#     else:
#         print('No se encontró la imagen del Vaper seleccionado')

# async def response_vapers(update: Update, context: CallbackContext):
#     query = update.callback_query
#     if query.data == 'close':
#         await context.bot.delete_message(query.message.chat_id, query.message.message_id)
#     elif query == 'main_menu':
#         await start(update, context)
#     elif query.data == 'vapers_1g':
#         await vapers_1g(update, context)
#     elif query.data == 'vapers_2g':
#         await vapers_2g(update, context)
#     else:
#         await selected_vaper(update, context)
#         return await send_vaper(update, context)

# Import libraries:
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile, Bot
from telegram.ext import CallbackContext

# Import Configure:
from paths_config import *
from start import start

# Constants:
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)

async def selected_vaper(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🗡Vapers 1 gramo", callback_data='vapers_1g')],
        [InlineKeyboardButton("⚔Vapers 2 gramos", callback_data='vapers_2g')],
        [InlineKeyboardButton("Volver al menú principal 🔙", callback_data='main_menu')],
        [InlineKeyboardButton("CERRAR ❌", callback_data='close')]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    m = '<b>Elige la cantidad de gramos:</b>'
    if update.message:
        await update.message.reply_text(m, reply_markup=markup, parse_mode='html')
    elif update.callback_query:
        await update.callback_query.message.edit_text(m, reply_markup=markup, parse_mode='html')

async def vapers_1g(update: Update, context: CallbackContext):
    keyboard_1g = [
        [InlineKeyboardButton("Lonzo Cream🍨", callback_data='vaper1')],
        [InlineKeyboardButton("Cali Connected🇨🇴🔥", callback_data='vaper2')],
        [InlineKeyboardButton("Gold Coast Clear Premiun🐻", callback_data='vaper3')],
        [InlineKeyboardButton("Tropical Gelato🍹", callback_data='vaper4')],
        [InlineKeyboardButton("Dosi Killer💀", callback_data='vaper5')],
        [InlineKeyboardButton("Volver al menú principal 🔙", callback_data='main_menu')],
        [InlineKeyboardButton("CERRAR ❌", callback_data='close')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard_1g)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Selecciona un botón para ver el Vaper:", reply_markup=reply_markup)

async def vapers_2g(update: Update, context: CallbackContext):
    keyboard_2g = [
        [InlineKeyboardButton("☠Packman: Moras🍇", callback_data='vaper6')],
        [InlineKeyboardButton("☠Packman: Moras azules🫐", callback_data='vaper7')],
        [InlineKeyboardButton("☠Packman: Chicle🍬", callback_data='vaper8')],
        [InlineKeyboardButton("☠Packman: Durazno🍑", callback_data='vaper9')],
        [InlineKeyboardButton("☠Packman: Piña🍍", callback_data='vaper10')],
        [InlineKeyboardButton("👾Backpack Boyz: Cereza🍒", callback_data='vaper11')],
        [InlineKeyboardButton("👾Backpack Boyz: Limón-cereza🍋🍒", callback_data='vaper12')],
        [InlineKeyboardButton("Volver al menú principal 🔙", callback_data='main_menu')],
        [InlineKeyboardButton("CERRAR ❌", callback_data='close')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard_2g)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Selecciona un botón para ver el Vaper:", 
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def send_vaper(update: Update, context: CallbackContext):
    query = update.callback_query
    vaper_selected = query.data
    vaper_image_path = None
    vaper_name = None
    back_callback = 'vapers_1g' if 'vaper' in vaper_selected and vaper_selected.replace('vaper', '').isdigit() and int(vaper_selected.replace('vaper', '')) <= 5 else 'vapers_2g'

    if vaper_selected == 'close':
        await context.bot.delete_message(query.message.chat_id, query.message.message_id)
    elif vaper_selected == 'vaper1':
        vaper_image_path = vaper_images[0]
        vaper_name = "Lonzo Cream 🍨⚡\nSativa\n1000 mg. de THC\n$1,200.00"
    elif vaper_selected == 'vaper2':
        vaper_image_path = vaper_images[1]
        vaper_name = "Cali Connected 🇨🇴🔥\nSativa\n1000 mg. de THC\n$1,200.00"
    elif vaper_selected == 'vaper3':
        vaper_image_path = vaper_images[2]
        vaper_name = "Gold Coast Clear Premiun 🐻👑\nIndica\n1000 mg. de THC\n$1,200.00"
    elif vaper_selected == 'vaper4':
        vaper_image_path = vaper_images[3]
        vaper_name = "Tropical Gelato 🏝🍹\nSativa\n1000 mg. de THC\n$1,200.00"
    elif vaper_selected == 'vaper5':
        vaper_image_path = vaper_images[4]
        vaper_name = "Dosi Killer 🐾\nSativa\n1000 mg. de THC\n$1,200.00"
    elif vaper_selected == 'vaper6':
        vaper_image_path = vaper_images2m[0]
        vaper_name = "Pack Man 💀\nSabor: Moras🍇\nIndica\n2000 mg. de THC\n$1,500.00"
    elif vaper_selected == 'vaper7':
        vaper_image_path = vaper_images2m[1]
        vaper_name = "Pack Man 💀\nSabor: Moras azules🫐\nSativa\n2000 mg. de THC\n$1,500.00"
    elif vaper_selected == 'vaper8':
        vaper_image_path = vaper_images2m[2]
        vaper_name = "Pack Man 💀\nSabor: Chicle🍬\nHíbrida\n2000 mg. de THC\n$1,500.00"
    elif vaper_selected == 'vaper9':
        vaper_image_path = vaper_images2m[3]
        vaper_name = "Pack Man 💀\nSabor: Durazno dulce🍑\nIndica\n2000 mg. de THC\n$1,500.00"
    elif vaper_selected == 'vaper10':
        vaper_image_path = vaper_images2m[4]
        vaper_name = "Pack Man 💀\nSabor: Piña agria🍍\nSativa\n2000 mg. de THC\n$1,500.00"
    elif vaper_selected == 'vaper11':
        vaper_image_path = vaper_images2m[5]
        vaper_name = "Backpack Boyz 👾🎒\nSabor: Cereza🍒\nDiamantes Líquidos\n2000 mg. de THC\n$1,500.00"
    elif vaper_selected == 'vaper12':
        vaper_image_path = vaper_images2m[6]
        vaper_name = "Pack Man 👾🎒\nSabor: Limón-cereza 🍒🍋\nDiamantes Líquidos\n2000 mg. de THC\n$1,500.00"

    if vaper_image_path:
        keyboard_back = [
            [InlineKeyboardButton("Volver al menú anterior 🔙", callback_data=back_callback)],
            [InlineKeyboardButton("Volver al menú principal 🔙", callback_data='main_menu')],
            [InlineKeyboardButton("CERRAR ❌", callback_data='close')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard_back)
        with open(vaper_image_path, 'rb') as image_file:
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=InputFile(image_file), caption=vaper_name, reply_markup=reply_markup)
    else:
        print('No se encontró la imagen del Vaper seleccionado')

async def response_vapers(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'close':
        await context.bot.delete_message(query.message.chat_id, query.message.message_id)
    elif query.data == 'main_menu':
        await start(update, context)
    elif query.data == 'vapers_1g':
        await vapers_1g(update, context)
    elif query.data == 'vapers_2g':
        await vapers_2g(update, context)
    else:
        await selected_vaper(update, context)
        return await send_vaper(update, context)
