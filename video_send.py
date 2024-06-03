# # Import Libraries:
# import os
# from dotenv import load_dotenv
# from telegram import Update, InputFile, Bot

# # Import configure:
# from paths_config import *

# # Constantes:
# load_dotenv()
# token = os.getenv('TOKEN')
# bot = Bot(token=token)

# # Función para enviar vídeo del catálogo
# async def send_catalog_video(update: Update):
#     if os.path.exists(video_path):
#         with open(video_path, 'rb') as video_file:
#             await bot.send_video(chat_id=update.message.chat_id, video=InputFile(video_file))
#     else:
#         print('No se encuentra el vídeo')

# async def send_bbd_video(update: Update):
#     if os.path.exists(bbd_video):
#         with open(bbd_video, 'rb') as video_file:
#             await bot.send_video(chat_id=update.message.chat_id, video=InputFile(video_file))
#     else:
#         print('No se encuentra el vídeo')

from telegram import Update, InputFile, Bot
from telegram.ext import CallbackContext
import os
from dotenv import load_dotenv

# Import Configure:
from paths_config import *

# Constantes:
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)

## Enviar video de BBD:
async def send_bbd_video(update: Update, context: CallbackContext):
    with open(bbd_video, 'rb') as video_file:
        await bot.send_video(chat_id=update.message.chat_id, video=InputFile(video_file))

## Enviar video de catálogo:
async def send_catalog_video(update: Update, context: CallbackContext):
    with open(video_path, 'rb') as video_file:
        await bot.send_video(chat_id=update.message.chat_id, video=InputFile(video_file))
