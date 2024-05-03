import os
from telegram.ext import CallbackContext, CallbackQueryHandler, filters
from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import InputFile 
from dotenv import load_dotenv


from text_processing import handle_response
from paths_config import *


# Create a new Web Server.
from fastapi import FastAPI, Request
from pydantic import BaseModel
from waitress import serve


# Constantes:
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)
web_server = FastAPI()

# Rutas:
# paths_config.py

# Definir Modelo de Pydantic:
class TelegramMessage(BaseModel):
    chat_id: int
    text: str
    

# Iniciamos la petición al servidor:
@web_server.post("/send_message/")
async def send_telegram_message(message: TelegramMessage):
    try:
        await bot.send_message(chat_id=message.chat_id, text=message.text)
        return {"message": "Mensaje enviado con éxito"}
    except Exception as e:
        return {"error": f"Error al enviar el mensaje: {e}"}



# Comandos:

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
        vaper_name = "Vaper 1 Gelatho $1,250.00"
    elif vaper_selected == 'vaper2':
        vaper_image_path = vaper_images[1]
        vaper_name = "Vaper 2 Flavors $1,320.00"
    elif vaper_selected == 'vaper3':
        vaper_image_path = vaper_images[2]
        vaper_name = "Vaper 3 Frost $1,450.00"
    elif vaper_selected == 'vaper4':
        vaper_image_path = vaper_images[3]
        vaper_name = "Vaper 4 Nova $1,585.00"
    elif vaper_selected == 'vaper5':
        vaper_image_path = vaper_images[4]
        vaper_name = "Vaper 5 Blaze $1,255.00"
        
    elif vaper_selected == 'vaper6':
        vaper_image_path = vaper_images[5]
        vaper_name = "Vaper 6 Blaze $1,255.00"
    elif vaper_selected == 'vaper7':
        vaper_image_path = vaper_images[6]
        vaper_name = "Vaper 7 Flavors $1,320.00"
    elif vaper_selected == 'vaper8':
        vaper_image_path = vaper_images[7]
        vaper_name = "Vaper 8 Frost $1,450.00"
    elif vaper_selected == 'vaper9':
        vaper_image_path = vaper_images[8]
        vaper_name = "Vaper 9 Nova $1,585.00"
    elif vaper_selected == 'vaper10':
        vaper_image_path = vaper_images[9]
        vaper_name = "Vaper 10 Blaze $1,255.00"
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

## Weed:
async def weed(update: Update, context: ContextTypes):
    # Crear el menú de selección de imágenes de cultivos.
    keyboard = [[InlineKeyboardButton(f"Weed {i}", callback_data=f'weed{i}')] for i in range(1, 6)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Contamos con diferentes tipos de Cultivos", reply_markup=reply_markup)

### Select Weed:
async def handle_weed_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    weed_selected = query.data
    weed_image_path = None
    weed_name = None
    
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
        with open(weed_image_path, 'rb') as image_file:
            await bot.send_photo(chat_id=query.message.chat_id, photo=InputFile(image_file), caption=weed_name)
    else:
        print('No se encontró la imagen del Cultivo de Weed seleccionado')


## Help:
async def help(update: Update, context: ContextTypes):
    await update.message.reply_text("Puedes iniciar la conversación con un Hola, y de ahí ir seleccionando la categoría. Comparte tus dudas: wa.link/7jvf7u 🫡")
    

## Custom Conversation:
# Now text_processing.py
# """response = handle_response()"""


## Respuestas a mensajes:
async def handle_message(update: Update, context: ContextTypes):
    message_type = update.message.chat.type
    text = update.message.text
    if message_type == 'private':  # Mensaje en chat privado
        text = update.message.text.lower() if update.message else None
    if message_type == 'group':
        if text.startswith(user_name):
            new_text = text.replace(user_name, '')
            response = handle_response(new_text, context, update)
        else:
            await update.message.reply_text("El bot solo responde a mensajes directos o comandos en grupos.")
            return
    elif text.lower() == 'hola':  # Agregado para mostrar el menú de inicio al decir "Hola"
        await start(update, context)
        return
    
    elif 'vapers' in text.lower() or '🚬' in text.lower():  # Modificación para responder al comando /vapers
        await vapers(update, context)
        return
    
    elif text.lower() == 'id':
        await update.message.reply_text(f"El ID de este chat es: {update.message.chat_id}")
        return
    
    elif 'candy' in text.lower() or 'dulces' in text.lower():  # Corrección en esta línea
        await candies(update, context)
        return
    
    elif 'weed' in text.lower() or 'cultivos' in text.lower(): # Agregado para responder al comando /weed
        await weed(update, context)
        return
    
    elif 'ayuda' in text.lower() or 'help' in text.lower():
        await help(update, context)
        return
    
    response = handle_response(text, context, update)  # Mover la asignación aquí para evitar el error

    if response is not None:
        await update.message.reply_text(response)
        if 'catalogo' in text.lower() or 'productos' in text.lower():
            await send_catalog_video(update)
        text = update.message.text

        # Verificar si el mensaje es "adiós" y enviar la imagen de despedida
    if 'bye' in text.lower() or '👋' in text.lower():
        if os.path.exists(image_bye):
            with open(image_bye, 'rb') as image_file:
                await bot.send_photo(chat_id=update.message.chat_id, photo=InputFile(image_file))
                
            # Verificar si el mensaje es "adiós" y enviar un vídeo de despedida
    if 'adios' in text.lower() or 'adiós' in text.lower():
        if os.path.exists(video_bye):
            with open(video_bye, 'rb') as video_file:
                await bot.send_video(chat_id=update.message.chat_id, video=InputFile(video_file))
    
    else:
        response = handle_response(text, context, update)

   
## Manejo de Errores:            
async def error(update: Update, context: ContextTypes):
    print(context.error)
    await update.message.reply_text('Ha ocurrido un error')

# Función para enviar vídeo del catálogo
async def send_catalog_video(update: Update):
    if os.path.exists(video_path):
        with open(video_path, 'rb') as video_file:
            await bot.send_video(chat_id=update.message.chat_id, video=InputFile(video_file))
    else:
        print('No se encuentra la imagen')

# Función para entregar el id del chat
async def handle_chat_id(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    await update.message.reply_text(f"El ID de este chat es: {chat_id}")


# Main:
if __name__ == '__main__':
    print('Iniciando Bot...')
    app = Application.builder().token(token).build()

    # Crear comandos y manejadores de callbacks:
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('vapers', vapers))
    app.add_handler(CommandHandler('type_vapers', type_vaper))
    app.add_handler(CommandHandler('candies', candies))
    app.add_handler(CommandHandler('catalogo', send_catalog_video))
    app.add_handler(CommandHandler('weed', weed))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('id', handle_chat_id))

    # Agregar los manejadores de CallbackQueryHandler:
    
    app.add_handler(CallbackQueryHandler(type_vaper, pattern=r'^vapers_\d+gm$'))
    app.add_handler(CallbackQueryHandler(handle_vaper_selection, pattern='vaper.*'))
    app.add_handler(CallbackQueryHandler(handle_candy_selection, pattern='candy.*'))
    app.add_handler(CallbackQueryHandler(handle_weed_selection, pattern='weed.*'))

    # Respuestas a mensajes:
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Manejo de errores:
    app.add_error_handler(error)

    # Iniciar bot:
    print('Bot iniciado')
    app.run_polling(poll_interval=1, timeout=10)