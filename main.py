# import os
# from telegram.ext import CallbackQueryHandler, filters, Application, CommandHandler, MessageHandler
# from telegram import Bot
# from dotenv import load_dotenv

# # Importar los comandos y funciones del bot
# from command_help import command_help
# from handle_chatId import handle_chat_id
# from handle_error import error
# from video_send import *
# from select_candy import *
# from select_vaper import *
# from select_w import *
# from start import start
# from handle_response import *
# from paths_config import *

# # Constantes
# load_dotenv()
# token = os.getenv('TOKEN')
# bot = Bot(token=token)

# # Main
# if __name__ == '__main__':
#     print('Iniciando Bot...')
#     app = Application.builder().token(token).build()

#     # Crear comandos y manejadores de callbacks
#     app.add_handler(CommandHandler('start', start))
#     app.add_handler(CommandHandler('vapers', selected_vaper))
#     app.add_handler(CommandHandler('candies', candies))
#     app.add_handler(CommandHandler('catalogo', send_catalog_video))
#     app.add_handler(CommandHandler('Donuts', send_bbd_video))
#     app.add_handler(CommandHandler('weed', weed))
#     app.add_handler(CommandHandler('help', command_help))
#     app.add_handler(CommandHandler('id', handle_chat_id))

#     # Agregar los manejadores de CallbackQueryHandler
#     app.add_handler(CallbackQueryHandler(response_vapers, pattern='vaper.*'))
#     app.add_handler(CallbackQueryHandler(response_vapers, pattern='close.*'))
#     app.add_handler(CallbackQueryHandler(start, pattern='main_menu.*'))
#     app.add_handler(CallbackQueryHandler(handle_candy_selection, pattern='candy.*'))
#     app.add_handler(CallbackQueryHandler(handle_weed_selection, pattern='weed.*'))

#     # Respuestas a mensajes
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))

#     # Manejo de errores
#     app.add_error_handler(error)

#     # Iniciar bot
#     print('Bot iniciado')
#     app.run_polling(poll_interval=1, timeout=10)

#     # Cerrar la conexión a la base de datos al finalizar el script
#     close_db_connection()

# import os
# from telegram.ext import CallbackQueryHandler, filters, Application, CommandHandler, MessageHandler
# from telegram import Bot
# from dotenv import load_dotenv

# # Importar los comandos y funciones del bot
# from command_help import command_help
# from handle_chatId import handle_chat_id
# from handle_error import error
# from video_send import *
# from select_candy import *
# from select_vaper import *
# from select_w import *
# from start import start
# from handle_response import handle_message, close_db_connection  # Importar handle_message y close_db_connection
# from paths_config import *

# # Constantes
# load_dotenv()
# token = os.getenv('TOKEN')
# bot = Bot(token=token)

# # Main
# if __name__ == '__main__':
#     print('Iniciando Bot...')
#     app = Application.builder().token(token).build()

#     # Crear comandos y manejadores de callbacks
#     app.add_handler(CommandHandler('start', start))
#     app.add_handler(CommandHandler('vapers', selected_vaper))
#     app.add_handler(CommandHandler('candies', candies))
#     app.add_handler(CommandHandler('catalogo', send_catalog_video))
#     app.add_handler(CommandHandler('Donuts', send_bbd_video))
#     app.add_handler(CommandHandler('weed', weed))
#     app.add_handler(CommandHandler('help', command_help))
#     app.add_handler(CommandHandler('id', handle_chat_id))

#     # Agregar los manejadores de CallbackQueryHandler
#     app.add_handler(CallbackQueryHandler(response_vapers, pattern='vaper.*'))
#     app.add_handler(CallbackQueryHandler(response_vapers, pattern='close.*'))
#     app.add_handler(CallbackQueryHandler(start, pattern='main_menu.*'))
#     app.add_handler(CallbackQueryHandler(handle_candy_selection, pattern='candy.*'))
#     app.add_handler(CallbackQueryHandler(handle_weed_selection, pattern='weed.*'))

#     # Respuestas a mensajes
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))

#     # Manejo de errores
#     app.add_error_handler(error)

#     # Iniciar bot
#     print('Bot iniciado')
#     app.run_polling(poll_interval=1, timeout=10)

#     # Cerrar la conexión a la base de datos al finalizar el script
#     close_db_connection()

import os
from telegram.ext import CallbackQueryHandler, filters, Application, CommandHandler, MessageHandler
from telegram import Bot
from dotenv import load_dotenv

# Importar los comandos y funciones del bot
from command_help import *
from handle_chatId import handle_chat_id
from handle_error import error
from video_send import *
from select_candy import *
from select_vaper import *
from select_w import *
from start import start, handler_start
from handle_response import handle_message, close_db_connection  # Importar handle_message y close_db_connection
from paths_config import *

# Constantes
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)

# Main
if __name__ == '__main__':
    print('Iniciando Bot...')
    app = Application.builder().token(token).build()

    # Crear comandos y manejadores de callbacks
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('vapers', selected_vaper))
    app.add_handler(CommandHandler('candies', candies))
    app.add_handler(CommandHandler('catalogo', send_catalog_video))
    app.add_handler(CommandHandler('Donuts', send_bbd_video))
    app.add_handler(CommandHandler('weed', weed))
    app.add_handler(CommandHandler('help', command_help))
    app.add_handler(CommandHandler('id', handle_chat_id))

    # Agregar los manejadores de CallbackQueryHandler
    app.add_handler(CallbackQueryHandler(response_vapers, pattern='vapers.*|vaper.*|close'))
    app.add_handler(CallbackQueryHandler(handler_start, pattern='^(vapers_menu|candies|weed|help)$'))
    app.add_handler(CallbackQueryHandler(handler_start, pattern='main_menu'))
    app.add_handler(CallbackQueryHandler(menu_callback, pattern='^(faq|contact)$'))
    app.add_handler(CallbackQueryHandler(handle_candy_selection, pattern='candy.*'))
    app.add_handler(CallbackQueryHandler(handle_weed_selection, pattern='weed.*'))

    # Respuestas a mensajes
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Manejo de errores
    app.add_error_handler(error)

    # Iniciar bot
    print('Bot iniciado')
    app.run_polling(poll_interval=1, timeout=10)

    # Cerrar la conexión a la base de datos al finalizar el script
    close_db_connection()

