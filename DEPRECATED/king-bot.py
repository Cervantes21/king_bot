# Import libraries:

import telebot as tme

# Create vars:

user = 'kings_mx_bot'
TOKEN = '7030212913:AAEvSDODlRFtKApMGEWyf8WiCj7pkr-H40s'

# Init bot
bot = tme.TeleBot(TOKEN, parse_mode=None)

# Define ours functions:

## Welcome print menu.
def main():    
    print('Hola, estás son las opciones: ')
    print('1. Vaporizadores')
    print('2. Dulces con THC')
    print('3. Cultivos especiales')

## Vapers
def menu_vapers():
    
    print('')

## Candies:

def menu_candies():
    
    print('')
     
# Special thinks.

def special_menu():
    pass

# Define bot:

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

# Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# - interval: int (default 0) - The interval between polling requests
# - timeout: integer (default 20) - Timeout in seconds for long polling.
# - allowed_updates: List of Strings (default None) - List of update types to request 
bot.infinity_polling(interval=0, timeout=20)

# getMe
user = bot.get_me()

# setWebhook
bot.set_webhook(url="https://linktr.ee/kinsboulevard", certificate=open('mycert.pem'))

# unset webhook
bot.remove_webhook()

# getUpdates
updates = bot.get_updates()
# or
updates = bot.get_updates(1234,100,20) #get_Updates(offset, limit, timeout):

# sendMessage
bot.send_message(chat_id, text)

# editMessageText
bot.edit_message_text(new_text, chat_id, message_id)

# forwardMessage
bot.forward_message(to_chat_id, from_chat_id, message_id)

# All send_xyz functions which can take a file as an argument, can also take a file_id instead of a file.
# sendPhoto
photo = open('/tmp/photo.png', 'rb')
bot.send_photo(chat_id, photo)
bot.send_photo(chat_id, "FILEID")

# sendAudio
audio = open('/tmp/audio.mp3', 'rb')
bot.send_audio(chat_id, audio)
bot.send_audio(chat_id, "FILEID")

## sendAudio with duration, performer and title.
bot.send_audio(CHAT_ID, file_data, 1, 'eternnoir', 'pyTelegram')

# sendVoice
voice = open('/tmp/voice.ogg', 'rb')
bot.send_voice(chat_id, voice)
bot.send_voice(chat_id, "FILEID")

# sendDocument
doc = open('/tmp/file.txt', 'rb')
bot.send_document(chat_id, doc)
bot.send_document(chat_id, "FILEID")

# sendSticker
sti = open('/tmp/sti.webp', 'rb')
bot.send_sticker(chat_id, sti)
bot.send_sticker(chat_id, "FILEID")

# sendVideo
video = open('/tmp/video.mp4', 'rb')
bot.send_video(chat_id, video)
bot.send_video(chat_id, "FILEID")

# sendVideoNote
videonote = open('/tmp/videonote.mp4', 'rb')
bot.send_video_note(chat_id, videonote)
bot.send_video_note(chat_id, "FILEID")

# sendLocation
bot.send_location(chat_id, lat, lon)

# sendChatAction
# action_string can be one of the following strings: 'typing', 'upload_photo', 'record_video', 'upload_video',
# 'record_audio', 'upload_audio', 'upload_document' or 'find_location'.
bot.send_chat_action(chat_id, action_string)

# getFile
# Downloading a file is straightforward
# Returns a File object
import requests
file_info = bot.get_file(file_id)

file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))

if __name__ == '__main__':
    pass

