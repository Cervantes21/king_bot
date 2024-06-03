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
#                 response_text = handle_response(telegram_update.chat_id, None, telegram_update.text)
#                 bot.send_message(chat_id=telegram_update.chat_id, text=response_text)
#                 return JSONResponse(status_code=200, content={"message": "Update processed successfully"})
#             else:
#                 return JSONResponse(status_code=200, content={"message": "Non-text update received"})
#         except Exception as e:
#             print("Error al procesar la solicitud:", e)
#             raise HTTPException(status_code=400, detail=str(e))
#     else:
#         raise HTTPException(status_code=415, detail="Unsupported Media Type")

# @web_server.post("/send_message/")
# async def send_telegram_message(message: TelegramMessage):
#     try:
#         await bot.send_message(chat_id=message.chat_id, text=message.text)
#         return {"message": "Mensaje enviado con éxito"}
#     except Exception as e:
#         return {"error": f"Error al enviar el mensaje: {e}"}

# def handle_response(chat_id, message_id, text):
#     processed_text = text.lower()
#     t = 'Un placer atenderte 😇🤌'
#     b = 'Adiós ✌👽'
#     print(processed_text)
#     if 'hola' in processed_text or '🖐' in processed_text:
#         return 'Hola, ¿Cómo puedo ayudarte? 🖐😋 Puedes decir "Quiero comprar" o enviar un "🚬"'
#     elif 'quiero comprar' in processed_text:
#         return 'Elige una opción del menú, o inicia con /start'
#     elif 'gracias' in processed_text or 'grax' in processed_text:
#         return t
#     elif 'thanks' in processed_text or '🙏' in processed_text:
#         return t
#     elif 'adios' in processed_text or 'adiós' in processed_text:
#         return b
#     elif 'bye' in processed_text or '👋' in processed_text:
#         return b
#     elif 'catalogo' in processed_text or 'productos' in processed_text:
#         return 'Enviando el catálogo...'
#     elif 'cigarro' in processed_text or ('cigarros' in processed_text and '🚬' in processed_text):
#         return '/vapers'
#     elif 'dulce' in processed_text or 'chocolate' in processed_text:
#         return '/candies'
#     elif '🆘' in processed_text or 'help' in processed_text:
#         return '¿En que necesitas ayuda? FAQ: 🧐 /help'
#     else:
#         return 'No te entiendo 😵‍💫 \n favor de presionar: /start' + '\n' + '😌 También puedes interactuar conmigo escribiendo "quiero comprar"' + '\n' '😬 También puedes usar palabras clave del producto que quieres. \n Ejemplo: "cigarro", o usar un Icono "🚬"'

# # Configurar ngrok
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
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import Json
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv('TOKEN')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

app = FastAPI(title='Kings_mx_bot', version='0.0.2')
application = Application.builder().token(TOKEN).build()

class TelegramMessage(BaseModel):
    update_id: int
    message: dict

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
            update = Update.de_json(json_body, application.bot)
            await application.process_update(update)
            return JSONResponse(content={"status": "ok"})
        except Exception as e:
            print(f"Error al procesar la solicitud: {e}")
            raise HTTPException(status_code=400, detail=f"Error: {e}")
