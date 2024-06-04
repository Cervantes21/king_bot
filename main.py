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
import os
import time
import asyncio
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from pyngrok import ngrok, conf
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from psycopg2.extras import Json
import psycopg2
from dotenv import load_dotenv
import uvicorn

# Import commands and functions for bot
from command_help import command_help
from handle_error import error
from video_send import *
from select_candy import *
from select_vaper import *
from select_w import *
from start import start
from handle_response import handle_message
from handle_chatId import handle_chat_id
# Paths and Configures:
from paths_config import *

# Load environment variables
load_dotenv()
NGROK_TOKEN = os.getenv('NGROK_TOKEN')
TOKEN = os.getenv('TOKEN')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Initialize bot and FastAPI application
bot = Bot(token=TOKEN)
app = FastAPI(title='Kings_mx_bot', version='0.0.2')

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

@app.post('/')
async def webhook(request: Request):
    if request.headers.get('content-type') == 'application/json':
        try:
            json_body = await request.json()
            print("Solicitud recibida:", json_body)
            update = Update.de_json(json_body, bot)
            await application.update_queue.put(update)
            return JSONResponse(status_code=200, content={"message": "Update processed successfully"})
        except Exception as e:
            print("Error al procesar la solicitud:", e)
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(status_code=415, detail="Unsupported Media Type")

async def configure_ngrok():
    conf.get_default().ngrok_token = NGROK_TOKEN
    ngrok_tunnel = ngrok.connect(5000)
    ngrok_url = ngrok_tunnel.public_url
    return ngrok_url

async def main():
    print('Iniciando Bot...')

    # Configure ngrok
    ngrok_url = await configure_ngrok()
    print(f"URL NGROK: {ngrok_url}")

    # Initialize the application
    global application
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Register commands;
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", command_help))
    application.add_handler(CommandHandler("id", handle_chat_id))
    application.add_handler(CommandHandler("candies", candies))
    application.add_handler(CommandHandler("vapers", selected_vaper))
    application.add_handler(CommandHandler("weed", weed))

    # Register CallbackQueryHandler:
    application.add_handler(CallbackQueryHandler(response_vapers, pattern='vaper.*'))
    application.add_handler(CallbackQueryHandler(response_vapers, pattern='close.*'))
    application.add_handler(CallbackQueryHandler(handle_candy_selection, pattern='candy.*'))
    application.add_handler(CallbackQueryHandler(handle_weed_selection, pattern='weed.*'))
    application.add_handler(CallbackQueryHandler(send_bbd_video, pattern='donas.*'))
    application.add_handler(CallbackQueryHandler(send_catalog_video, pattern=r'catalogo.*'))
    # application.add_handler(CallbackQueryHandler(send_catalog_video, pattern='catalogo.*'))
    # Response to menssage:
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    # Error Handler:
    application.add_error_handler(error)

    # Set webhook
    await application.bot.delete_webhook()
    time.sleep(1)
    await application.bot.set_webhook(url=ngrok_url)

    print('Bot iniciado')

    # Start the bot and FastAPI server
    await application.initialize()
    await application.start()

    config = uvicorn.Config(app, host="0.0.0.0", port=5000)
    server = uvicorn.Server(config)
    
    bot_task = asyncio.create_task(application.updater.start_polling())
    server_task = asyncio.create_task(server.serve())

    await asyncio.gather(bot_task, server_task)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot detenido")

