# # Import libraries:
# import os
# from dotenv import load_dotenv
# from telegram import Update, InputFile, Bot
# from telegram.ext import ContextTypes

# # Import Configure:
# from paths_config import *
# from text_processing import handle_response
# from select_vaper import *
# from select_w import *
# from select_candy import *
# from video_send import *
# from start import start
# from command_help import command_help

# # Constantes:
# load_dotenv()
# token = os.getenv('TOKEN')
# bot = Bot(token=token)


# # Create list of words:

# welcome_words = [
#     'hola', 'hi', 'menú', 'menu', '✌'
#     'hoooola', 'hols', 'holi', 'que onda',
#     'holis', '😀','😃','😄','😁','🖐','🖖',
#     '🖐','🫰','🤟','😎','🔥','❤','❤️‍🔥','👀'
# ]

# candy_words = [
#     'candy','dulces','🍬','dulce',
#     'chocolate','candies','🍫','🍭',
#     'gomitas', 'jolly', 'thc', 'candies'
# ]

# weed_words = [
#     'weed', 'cultivos', '🤙', '🍂',
#     'mota', 'mosh', 'gramos', 'cultivo',
#     '🌱', '💚', 'green', '🍀','🍁', 'fumar'
# ]

# vapers_words = [
#     'vapers', 'vaper', 'cigarro',
#     'cigui', 'electronico' 'electrónico',
#     '🚬', 'smoke', 'fumar', 'vapear'
# ]

# thanks_words = [
#     'gracias', 'thanks', 'grax', 'agradecido',
#     '🙏','🫶','👍','👏', 'thank you', 'grscias'
#     'gracia', 'graciotas'
# ]


# ## Respuestas a mensajes:
# async def handle_message(update: Update, context: ContextTypes):
#     message_type = update.message.chat.type
#     user_name = update.message.chat.username
#     text = update.message.text
#     if message_type == 'private':  # Mensaje en chat privado
#         text = update.message.text.lower() if update.message else None
#     if message_type == 'group':
#         if text.startswith(user_name):
#             new_text = text.replace(user_name, '')
#             response = handle_response(new_text, context, update)
#         else:
#             await update.message.reply_text("El bot solo responde a mensajes directos o comandos en grupos.")
#             return
        
#     elif any(word in text.lower() for word in welcome_words):
#         await start(update, context)
#         return
    
#     elif text.lower() == 'id':
#         await update.message.reply_text(f"El ID de este chat es: {update.message.chat_id}")
#         return
    
#     elif any(word in text.lower() for word in candy_words):
#         await candies(update, context)
#         return
    
#     elif any(word in text.lower() for word in weed_words):
#         await weed(update, context)
#         return
    
#     elif any(word in text.lower() for word in vapers_words):
#         await selected_vaper(update, context)
#         return

#     elif 'ayuda' in text.lower() or 'help' in text.lower():
#         await command_help(update, context)
#         return
    
#     elif 'donas' in text.lower() or 'donuts' in text.lower():
#         await send_bbd_video(update)
#         return
    
#     response = handle_response(text, context, update)

#     if response is not None:
#         await update.message.reply_text(response)
#         if 'catálogo' in text.lower() or 'catalogo' in text.lower():
#             await send_catalog_video(update)
#         text = update.message.text
        
#     elif response is not None:
#         await update.message.reply_text(response)
#         if 'productos' in text.lower() or 'producto' in text.lower():
#             await send_catalog_video(update)
#         text = update.message.text

#         # Verificar si el mensaje es "adiós" y enviar la imagen de despedida
#     if 'bye' in text.lower() or '👋' in text.lower():
#         if os.path.exists(image_bye):
#             with open(image_bye, 'rb') as image_file:
#                 await bot.send_photo(chat_id=update.message.chat_id, photo=InputFile(image_file))
                
#             # Verificar si el mensaje es "adiós" y enviar un vídeo de despedida
#     if 'adios' in text.lower() or 'adiós' in text.lower():
#         if os.path.exists(video_bye):
#             with open(video_bye, 'rb') as video_file:
#                 await bot.send_video(chat_id=update.message.chat_id, video=InputFile(video_file))
    
#     elif any(word in text.lower() for word in thanks_words):
#         if os.path.exists(thanks):
#             with open(thanks, 'rb') as image_file:
#                 await bot.send_photo(chat_id=update.message.chat_id, photo=InputFile(image_file))
     
#     else:
#         response = handle_response(text, context, update)

# Import libraries:
import os
import sqlite3
from datetime import datetime
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
from command_help import command_help

# Constantes:
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)

# Conectar a la base de datos y crear la tabla si no existe
conn = sqlite3.connect('conversations.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS conversations (
    user_name TEXT,
    user_id INTEGER,
    date TEXT,
    message TEXT,
    chat_id INTEGER,
    message_id INTEGER,
    response TEXT
)
''')
conn.commit()

# Función para guardar la conversación en la base de datos
def save_conversation(user_name, user_id, date, message, chat_id, message_id, response):
    cursor.execute('''
    INSERT INTO conversations (user_name, user_id, date, message, chat_id, message_id, response)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_name, user_id, date, message, chat_id, message_id, response))
    conn.commit()

# Create list of words:
welcome_words = [
    'hola', 'hi', 'menú', 'menu', '✌',
    'hoooola', 'hols', 'holi', 'que onda',
    'holis', '😀','😃','😄','😁','🖐','🖖',
    '🖐','🫰','🤟','😎','🔥','❤','❤️‍🔥','👀'
]

candy_words = [
    'candy','dulces','🍬','dulce',
    'chocolate','candies','🍫','🍭',
    'gomitas', 'jolly', 'thc', 'candies'
]

weed_words = [
    'weed', 'cultivos', '🤙', '🍂',
    'mota', 'mosh', 'gramos', 'cultivo',
    '🌱', '💚', 'green', '🍀','🍁', 'fumar'
]

vapers_words = [
    'vapers', 'vaper', 'cigarro',
    'cigui', 'electronico', 'electrónico',
    '🚬', 'smoke', 'fumar', 'vapear'
]

thanks_words = [
    'gracias', 'thanks', 'grax', 'agradecido',
    '🙏','🫶','👍','👏', 'thank you', 'grscias',
    'gracia', 'graciotas'
]

# Función para manejar los mensajes
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    user = update.message.from_user
    user_name = user.username
    user_id = user.id
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = update.message.text
    chat_id = update.message.chat_id
    message_id = update.message.message_id

    if message_type == 'private':  # Mensaje en chat privado
        text = update.message.text.lower() if update.message else None
    elif message_type == 'group':
        if message.startswith(user_name):
            new_text = message.replace(user_name, '')
            response = handle_response(new_text, context, update)
        else:
            await update.message.reply_text("El bot solo responde a mensajes directos o comandos en grupos.")
            return
    else:
        text = message.lower() if message else None

    response = None
    if any(word in text for word in welcome_words):
        await start(update, context)
    elif text == 'id':
        await update.message.reply_text(f"El ID de este chat es: {update.message.chat_id}")
    elif any(word in text for word in candy_words):
        await candies(update, context)
    elif any(word in text for word in weed_words):
        await weed(update, context)
    elif any(word in text for word in vapers_words):
        await selected_vaper(update, context)
    elif 'ayuda' in text or 'help' in text:
        await command_help(update, context)
    elif 'donas' in text or 'donuts' in text:
        await send_bbd_video(update)
    else:
        response = handle_response(text, context, update)
        if response:
            await update.message.reply_text(response)
            if 'catálogo' in text or 'catalogo' in text:
                await send_catalog_video(update)
            if 'productos' in text or 'producto' in text:
                await send_catalog_video(update)
        if 'bye' in text or '👋' in text:
            if os.path.exists(image_bye):
                with open(image_bye, 'rb') as image_file:
                    await bot.send_photo(chat_id=update.message.chat_id, photo=InputFile(image_file))
        if 'adios' in text or 'adiós' in text:
            if os.path.exists(video_bye):
                with open(video_bye, 'rb') as video_file:
                    await bot.send_video(chat_id=update.message.chat_id, video=InputFile(video_file))
        if any(word in text for word in thanks_words):
            if os.path.exists(thanks):
                with open(thanks, 'rb') as image_file:
                    await bot.send_photo(chat_id=update.message.chat_id, photo=InputFile(image_file))

    # Guardar la conversación en la base de datos
    save_conversation(user_name, user_id, date, message, chat_id, message_id, response)

# Cerrar la conexión a la base de datos al finalizar el script
def close_db_connection():
    conn.close()
