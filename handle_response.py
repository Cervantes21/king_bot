# Import libraries:
import os
from dotenv import load_dotenv
from telegram import Update, InputFile, Bot
from telegram.ext import ContextTypes

# Import Configure:
from paths_config import *
from text_processing import handle_response
from select_vaper import *
from select_w import *
from select_candy import *
from video_send import *
from start import start

# Constantes:
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)


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
    
    elif 'vaper' in text.lower():
        await type_vaper(update, context)
        print(f'La Elección es: {text}')
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
    
    elif 'donas' in text.lower() or 'donuts' in text.lower():
        await send_bbd_video(update)
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