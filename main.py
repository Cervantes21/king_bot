# # Import libraries:
# import os
# from telegram.ext import CallbackQueryHandler, filters, Application, CommandHandler, MessageHandler
# from telegram import Bot
# from dotenv import load_dotenv

# # Commands and functions for bot:
# from command_help import command_help
# from handle_chatId import handle_chat_id
# from handle_error import error
# from video_send import *
# from select_candy import *
# from select_vaper import *
# from select_w import *
# from start import start
# from handle_response import handle_message


# # Paths and Configures:
# from paths_config import *

# # Constantes:
# load_dotenv()
# token = os.getenv('TOKEN')
# bot = Bot(token=token)


# # Main:
# if __name__ == '__main__':
#     print('Iniciando Bot...')
#     app = Application.builder().token(token).build()

#     # Crear comandos y manejadores de callbacks:
#     app.add_handler(CommandHandler('start', start))
#     app.add_handler(CommandHandler('vapers', selected_vaper))
#     app.add_handler(CommandHandler('candies', candies))
#     app.add_handler(CommandHandler('catalogo', send_catalog_video))
#     app.add_handler(CommandHandler('Donuts', send_bbd_video))
#     app.add_handler(CommandHandler('weed', weed))
#     app.add_handler(CommandHandler('help', command_help))
#     app.add_handler(CommandHandler('id', handle_chat_id))

#     # Agregar los manejadores de CallbackQueryHandler:
    
#     app.add_handler(CallbackQueryHandler(response_vapers, pattern='vaper.*'))
#     app.add_handler(CallbackQueryHandler(response_vapers, pattern='close.*'))
#     app.add_handler(CallbackQueryHandler(handle_candy_selection, pattern='candy.*'))
#     app.add_handler(CallbackQueryHandler(handle_weed_selection, pattern='weed.*'))

#     # Respuestas a mensajes:
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))

#     # Manejo de errores:
#     app.add_error_handler(error)

#     # Iniciar bot:
#     print('Bot iniciado')
#     app.run_polling(poll_interval=1, timeout=10)

# import os
# import time
# import telebot
# from fastapi import FastAPI, Request, HTTPException
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
# from pyngrok import ngrok, conf
# import uvicorn
# import psycopg2
# from psycopg2.extras import Json
# from dotenv import load_dotenv

# # Commands and functions for bot:
# from command_help import command_help
# from handle_chatId import handle_chat_id
# from handle_error import error
# from video_send import *
# from select_candy import *
# from select_vaper import *
# from select_w import *
# from start import start
# from handle_response import handle_response

# # Paths and Configures:
# from paths_config import *

# # Cargar variables de entorno
# load_dotenv()
# NGROK_TOKEN = os.getenv('NGROK_TOKEN')
# TOKEN = os.getenv('TOKEN')
# DB_HOST = os.getenv('DB_HOST', 'localhost')
# DB_NAME = os.getenv('DB_NAME')
# DB_USER = os.getenv('DB_USER')
# DB_PASSWORD = os.getenv('DB_PASSWORD')

# bot = telebot.TeleBot(token=TOKEN)
# web_server = FastAPI(title='Kings_mx_bot', version='0.0.2')

# class TelegramMessage(BaseModel):
#     chat_id: int
#     text: str

# def connect_db():
#     return psycopg2.connect(
#         host=DB_HOST,
#         dbname=DB_NAME,
#         user=DB_USER,
#         password=DB_PASSWORD
#     )

# def save_message(chat_id, text):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute("SELECT messages FROM conversations WHERE user_id = %s", (chat_id,))
#     result = cur.fetchone()

#     if result:
#         messages = result[0]
#         messages.append(text)
#         cur.execute("UPDATE conversations SET messages = %s WHERE user_id = %s", (Json(messages), chat_id))
#     else:
#         cur.execute("INSERT INTO conversations (user_id, messages) VALUES (%s, %s)", (chat_id, Json([text])))

#     conn.commit()
#     cur.close()
#     conn.close()

# @web_server.post('/')
# async def webhook(request: Request):
#     if request.headers.get('content-type') == 'application/json':
#         try:
#             json_body = await request.json()
#             print("Solicitud recibida:", json_body)
#             if 'message' in json_body and 'text' in json_body['message']:
#                 telegram_update = TelegramMessage(chat_id=json_body['message']['chat']['id'], text=json_body['message']['text'])
#                 save_message(telegram_update.chat_id, telegram_update.text)
#                 response_text = handle_response(telegram_update.text, None, None)
#                 bot.send_message(chat_id=telegram_update.chat_id, text=response_text)
#                 return JSONResponse(status_code=200, content={"message": "Update processed successfully"})
#             else:
#                 return JSONResponse(status_code=200, content={"message": "Non-text update received"})
#         except Exception as e:
#             print("Error al procesar la solicitud:", e)
#             raise HTTPException(status_code=400, detail=str(e))
#     else:
#         raise HTTPException(status_code=415, detail="Unsupported Media Type")

# def configure_ngrok():
#     conf.get_default().config_path = "./config_ngrok.yml"
#     conf.get_default().region = "us"
#     ngrok.set_auth_token(NGROK_TOKEN)
#     ngrok_tunnel = ngrok.connect(5000, bind_tls=True)
#     ngrok_url = ngrok_tunnel.public_url
#     return ngrok_url

# if __name__ == '__main__':
#     print('Iniciando Bot...')
#     ngrok_url = configure_ngrok()
#     print("URL NGROK:", ngrok_url)
#     bot.delete_webhook()
#     time.sleep(1)
#     bot.set_webhook(url=ngrok_url)
#     uvicorn.run(web_server, host="0.0.0.0", port=5000)
  
import os
import time
from telegram import Bot
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pyngrok import ngrok, conf
import uvicorn
import psycopg2
from psycopg2.extras import Json
from dotenv import load_dotenv

# Commands and functions for bot:
from command_help import command_help
from handle_chatId import handle_chat_id
from handle_error import error
from video_send import send_bbd_video, send_catalog_video
from select_candy import candies, handle_candy_selection
from select_vaper import selected_vaper, response_vapers
from select_w import weed, handle_weed_selection
from start import start
from handle_response import handle_response

# Paths and Configures:
from paths_config import image_bye, video_bye, thanks

# Cargar variables de entorno
load_dotenv()
NGROK_TOKEN = os.getenv('NGROK_TOKEN')
TOKEN = os.getenv('TOKEN')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

bot = telebot.TeleBot(token=TOKEN)
web_server = FastAPI(title='Kings_mx_bot', version='0.0.2')

class TelegramMessage(BaseModel):
    chat_id: int
    text: str

def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def save_message(chat_id, text):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT messages FROM conversations WHERE user_id = %s", (chat_id,))
    result = cur.fetchone()

    if result:
        messages = result[0]
        messages.append(text)
        cur.execute("UPDATE conversations SET messages = %s WHERE user_id = %s", (Json(messages), chat_id))
    else:
        cur.execute("INSERT INTO conversations (user_id, messages) VALUES (%s, %s)", (chat_id, Json([text])))

    conn.commit()
    cur.close()
    conn.close()

@web_server.post('/')
async def webhook(request: Request):
    if request.headers.get('content-type') == 'application/json':
        try:
            json_body = await request.json()
            print("Solicitud recibida:", json_body)
            if 'message' in json_body and 'text' in json_body['message']:
                telegram_update = TelegramMessage(chat_id=json_body['message']['chat']['id'], text=json_body['message']['text'])
                save_message(telegram_update.chat_id, telegram_update.text)
                handle_telegram_message(telegram_update.chat_id, telegram_update.text)
                return JSONResponse(status_code=200, content={"message": "Update processed successfully"})
            elif 'callback_query' in json_body:
                chat_id = json_body['callback_query']['message']['chat']['id']
                data = json_body['callback_query']['data']
                if 'candy' in data:
                    handle_candy_selection(chat_id, data)
                elif 'weed' in data:
                    handle_weed_selection(chat_id, data)
                else:
                    response_vapers(chat_id, data)
                return JSONResponse(status_code=200, content={"message": "Callback processed successfully"})
            else:
                return JSONResponse(status_code=200, content={"message": "Non-text update received"})
        except Exception as e:
            print("Error al procesar la solicitud:", e)
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(status_code=415, detail="Unsupported Media Type")

def handle_telegram_message(chat_id, text):
    text_lower = text.lower()
    
    if text_lower == 'hola':
        start(chat_id)
    elif 'vapers' in text_lower or '🚬' in text_lower:
        selected_vaper(chat_id)
    elif text_lower == 'id':
        bot.send_message(chat_id, f"El ID de este chat es: {chat_id}")
    elif 'candy' in text_lower or 'dulces' in text_lower:
        candies(chat_id)
    elif 'weed' in text_lower or 'cultivos' in text_lower:
        weed(chat_id)
    elif 'ayuda' in text_lower or 'help' in text_lower:
        command_help(chat_id)
    elif 'donas' in text_lower or 'donuts' in text_lower:
        send_bbd_video(chat_id)
    else:
        response_text = handle_response(text, None, None)
        bot.send_message(chat_id, text=response_text)
        additional_actions(chat_id, text_lower)

def additional_actions(chat_id, text):
    if 'bye' in text or '👋' in text:
        if os.path.exists(image_bye):
            with open(image_bye, 'rb') as image_file:
                bot.send_photo(chat_id, photo=image_file)
    elif 'adios' in text or 'adiós' in text:
        if os.path.exists(video_bye):
            with open(video_bye, 'rb') as video_file:
                bot.send_video(chat_id, video=video_file)
    elif 'gracias' in text or 'grax' in text or 'thanks' in text or '🙏' in text:
        if os.path.exists(thanks):
            with open(thanks, 'rb') as image_file:
                bot.send_photo(chat_id, photo=image_file)

def configure_ngrok():
    conf.get_default().config_path = "./config_ngrok.yml"
    conf.get_default().region = "us"
    ngrok.set_auth_token(NGROK_TOKEN)
    ngrok_tunnel = ngrok.connect(5000, bind_tls=True)
    ngrok_url = ngrok_tunnel.public_url
    return ngrok_url

if __name__ == '__main__':
    print('Iniciando Bot...')
            # Configurar el bot
    bot = Bot(token=TOKEN)
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Configurar ngrok
    conf.get_default().ngrok_token = NGROK_TOKEN
    public_url = ngrok.connect(5000).public_url
    bot.set_webhook(url=public_url)

# Registrar comandos y manejadores
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", command_help))
    application.add_handler(CallbackQueryHandler(handle_response))
    application.add_handler(CommandHandler("bbd_video", send_bbd_video))
    application.add_handler(CommandHandler("catalog_video", send_catalog_video))
    application.add_handler(CommandHandler("candies", candies))
    application.add_handler(CommandHandler("vapers", selected_vaper))
    application.add_handler(CommandHandler("weed", weed))
    application.add_handler(CommandHandler('id', handle_chat_id))

    application.add_handler(CallbackQueryHandler(response_vapers, pattern='vaper.*'))
    application.add_handler(CallbackQueryHandler(response_vapers, pattern='close.*'))
    application.add_handler(CallbackQueryHandler(handle_candy_selection, pattern='candy.*'))
    application.add_handler(CallbackQueryHandler(handle_weed_selection, pattern='weed.*'))

    application.add_handler(CallbackQueryHandler(response_vapers))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    application.add_error_handler(error)
    ngrok_url = configure_ngrok()
    print("URL NGROK:", ngrok_url)
    bot.delete_webhook()
    time.sleep(1)
    bot.set_webhook(url=ngrok_url)
    
    print('Bot iniciado')
    uvicorn.run(web_server, host="0.0.0.0", port=5000)
