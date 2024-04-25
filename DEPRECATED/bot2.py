# Import Libraries:
import os
import asyncio
from telegram import Bot
from telegram import InputFile

#Define Paths
bot = Bot(token = '7030212913:AAEvSDODlRFtKApMGEWyf8WiCj7pkr-H40s')
chat_id = '-1002045025298' #Group
image_path = './BOULEVARD/GFgEEU-WUAExx4B.jpeg'
#image_path = './BOULEVARD/candies.jpeg'
# Async function to send photo
async def send_photo_async():
    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            await bot.send_photo(chat_id=chat_id, photo=InputFile(image_file))
    else:
        print('No se encuentra la imagen')

# Run the async function
asyncio.run(send_photo_async())
