# Import libraries:
import os
from telegram.ext import CallbackQueryHandler, filters, Application, CommandHandler, MessageHandler
from telegram import Bot
from dotenv import load_dotenv

# Commands and functions for bot:
from command_help import help
from handle_chatId import handle_chat_id
from handle_error import error
from video_send import *
from select_candy import *
from select_vaper import *
from select_w import *
from start import start
from handle_response import handle_message

# Create a new Web Server.
from fastapi import FastAPI, Request
from pydantic import BaseModel
from waitress import serve

# Paths and Configures:
from paths_config import *

# Constantes:
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)
web_server = FastAPI()

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



# Main:
if __name__ == '__main__':
    print('Iniciando Bot...')
    app = Application.builder().token(token).build()

    # Crear comandos y manejadores de callbacks:
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('vapers', selected_vaper))
    app.add_handler(CommandHandler('candies', candies))
    app.add_handler(CommandHandler('catalogo', send_catalog_video))
    app.add_handler(CommandHandler('Donuts', send_bbd_video))
    app.add_handler(CommandHandler('weed', weed))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('id', handle_chat_id))

    # Agregar los manejadores de CallbackQueryHandler:
    
    app.add_handler(CallbackQueryHandler(response_vapers, pattern='vaper.*'))
    app.add_handler(CallbackQueryHandler(response_vapers, pattern='close.*'))
    app.add_handler(CallbackQueryHandler(handle_candy_selection, pattern='candy.*'))
    app.add_handler(CallbackQueryHandler(handle_weed_selection, pattern='weed.*'))

    # Respuestas a mensajes:
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Manejo de errores:
    app.add_error_handler(error)

    # Iniciar bot:
    print('Bot iniciado')
    app.run_polling(poll_interval=1, timeout=10)