import os
from telegram.ext import CallbackContext, CallbackQueryHandler, filters
from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import InputFile 
from dotenv import load_dotenv
# Variables:
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)
# Rutas:
PATH = './BOULEVARD'
vapers_path = PATH + '/vapers'
candy_path = PATH + '/candy'
weed_path = PATH + '/weed'
image_path = PATH + '/Asset-2.jpeg'
image_bye = PATH + '/GFgEEU-WUAExx4B.jpeg'

# Vapers
vaper1 = vapers_path + '/vaper1.png'
vaper2 = vapers_path + '/vaper2.png'
vaper3 = vapers_path + '/vaper3.png'
vaper4 = vapers_path + '/vaper4.png'
vaper5 = vapers_path + '/vaper5.png'

# Candies:
candy1 = candy_path + '/candy1.jpeg'
candy2 = candy_path + '/candy2.jpeg'
candy3 = candy_path + '/candy3.jpeg'
candy4 = candy_path + '/candy4.jpeg'

# Weed
weed1 = weed_path + '/weed1.jpg'
weed2 = weed_path + '/weed2.jpg'
weed3 = weed_path + '/weed3.jpg'
weed4 = weed_path + '/weed4.jpg'
weed5 = weed_path + '/weed5.jpg'

# Comandos:

# Comandos:
# async def start(update: Update, context: ContextTypes):
#     # Crear los botones
#     keyboard = [
#         ['Vapers', 'Dulces'],
#         ['Cultivos', 'Ayuda']
#     ]
#     # Adjuntar los botones al mensaje de bienvenida
#     reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
#     await update.message.reply_text("Hola, soy un King. ¿En qué puedo ayudarte?\nElige una opción:", reply_markup=reply_markup)

async def start(update: Update, context: ContextTypes):
    # Crear los botones
    keyboard = [
        [InlineKeyboardButton("Vapers", callback_data='vapers')],
        [InlineKeyboardButton("Dulces con THC", callback_data='candies')],
        [InlineKeyboardButton("Cultivos", callback_data='weed')],
        [InlineKeyboardButton("Ayuda", callback_data='help')]
    ]
    # Adjuntar los botones al mensaje de bienvenida
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Hola, soy un King. ¿En qué puedo ayudarte?\nElige una opción:", reply_markup=reply_markup)


## Vapers:
async def vapers(update: Update, context: ContextTypes):
    # Crear el menú de selección de imágenes de Vapers
    keyboard = [
        [InlineKeyboardButton("Vaper 1", callback_data='vaper1')],
        [InlineKeyboardButton("Vaper 2", callback_data='vaper2')],
        [InlineKeyboardButton("Vaper 3", callback_data='vaper3')],
        [InlineKeyboardButton("Vaper 4", callback_data='vaper4')],
        [InlineKeyboardButton("Vaper 5", callback_data='vaper5')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Selecciona un tipo de Vaper:", reply_markup=reply_markup)

### Select Vaper:
async def handle_vaper_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    vaper_selected = query.data
    vaper_image_path = None
    
    if vaper_selected == 'vaper1':
        vaper_image_path = vaper1
    elif vaper_selected == 'vaper2':
        vaper_image_path = vaper2
    elif vaper_selected == 'vaper3':
        vaper_image_path = vaper3
    elif vaper_selected == 'vaper4':
        vaper_image_path = vaper4
    elif vaper_selected == 'vaper5':
        vaper_image_path = vaper5

    if vaper_image_path:
        with open(vaper_image_path, 'rb') as image_file:
            await bot.send_photo(chat_id=query.message.chat_id, photo=InputFile(image_file))
    else:
        print('No se encontró la imagen del Vaper seleccionado')

## Candies:

async def candies(update: Update, context: ContextTypes):
    # Crear el menú de selección de imágenes de Dulces con THC
    keyboard = [
        [InlineKeyboardButton("Candy 1", callback_data='candy1')],
        [InlineKeyboardButton("Candy 2", callback_data='candy2')],
        [InlineKeyboardButton("Candy 3", callback_data='candy3')],
        [InlineKeyboardButton("Candy 4", callback_data='candy4')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Selecciona un tipo de Dulces con THC:", reply_markup=reply_markup)

### Select Candy:
async def handle_candy_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    candy_selected = query.data
    candy_image_path = None
    
    if candy_selected == 'candy1':
        candy_image_path = candy1
    elif candy_selected == 'candy2':
        candy_image_path = candy2
    elif candy_selected == 'candy3':
        candy_image_path = candy3
    elif candy_selected == 'candy4':
        candy_image_path = candy4

    if candy_image_path:
        with open(candy_image_path, 'rb') as image_file:
            await bot.send_photo(chat_id=query.message.chat_id, photo=InputFile(image_file))
    else:
        print('No se encontró la imagen del Dulce con THC seleccionado')

## Weed:
async def weed(update: Update, context: ContextTypes):
    # Crear el menú de selección de imágenes de Vapers
    keyboard = [
        [InlineKeyboardButton("Weed 1", callback_data='weed1')],
        [InlineKeyboardButton("Weed 2", callback_data='weed2')],
        [InlineKeyboardButton("Weed 3", callback_data='weed3')],
        [InlineKeyboardButton("Weed 4", callback_data='weed4')],
        [InlineKeyboardButton("Weed 5", callback_data='weed5')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Contamos con diferentes tipos de Cultivos", reply_markup=reply_markup)

async def handle_weed_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    weed_selected = query.data
    weed_image_path = None
    
    if weed_selected == 'weed1':
        weed_image_path = weed1
    elif weed_selected == 'weed2':
        weed_image_path = weed2
    elif weed_selected == 'weed3':
        weed_image_path = weed3
    elif weed_selected == 'weed4':
        weed_image_path = weed4
    elif weed_selected == 'weed5':
        weed_image_path = weed5

    if weed_image_path:
        with open(weed_image_path, 'rb') as image_file:
            await bot.send_photo(chat_id=query.message.chat_id, photo=InputFile(image_file))
    else:
        print('No se encontró la imagen del Cultivo de Weed seleccionado')

## Help:
async def help(update: Update, context: ContextTypes):
    await update.message.reply_text('Comparte tus dudas: wa.link/7jvf7u 🫡')

## Custom Conversation:
def handle_response(text: str, context: ContextTypes, update: Update):
    processed_text = text.lower()
    print(processed_text)
    if 'hola' in processed_text:
        return 'Hola, ¿Cómo puedo ayudarte?'
    elif 'quiero comprar' in processed_text:
        return 'Elige una opción del menú, o inicia con /start'
    
    elif 'gracias' in processed_text:
        return 'Un placer atenderte 😇🤌'
    
    elif 'adios' in processed_text:
        return 'Adiós'
    elif 'catalogo' in processed_text or 'productos' in processed_text:
        return 'Enviando el catálogo...'
   
    elif 'vaper' in processed_text or 'cigarros' in processed_text:
        return '/vapers'
    elif 'dulces' in processed_text or 'candy' in processed_text:
        return '/candies'
    elif 'ayuda' in processed_text or 'help' in processed_text:
        return '¿En que necesitas ayuda? FAQ: /help'
    else:
        return 'No te entiendo, favor de presionar: /start'


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
    
    elif text.lower() == 'vapers':  # Modificación para responder al comando /vapers
        await vapers(update, context)
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
    
    response = handle_response(text, context, update)  # Mover la asignación aquí para evitar el error

    if response is not None:
        await update.message.reply_text(response)
        if 'catalogo' in text.lower() or 'productos' in text.lower():
            await send_catalog_image(update)
        text = update.message.text

        # Verificar si el mensaje es "adiós" y enviar la imagen de despedida
    if text.lower() == 'adios':
        if os.path.exists(image_bye):
            with open(image_bye, 'rb') as image_file:
                await bot.send_photo(chat_id=update.message.chat_id, photo=InputFile(image_file))
    else:
        response = handle_response(text, context, update)

   
## Manejo de Errores:            
async def error(update: Update, context: ContextTypes):
    print(context.error)
    await update.message.reply_text('Ha ocurrido un error')

# Función para enviar la imagen del catálogo
async def send_catalog_image(update: Update):
    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            await bot.send_photo(chat_id=update.message.chat_id, photo=InputFile(image_file))
    else:
        print('No se encuentra la imagen')

# Función para entregar el id del chat
async def handle_chat_id(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    await update.message.reply_text(f"El ID de este chat es: {chat_id}")


# Main:
if __name__ == '__main__':
    print('Iniciando Bot...')
    app = Application.builder().token(token).build()

    # Crear comandos y manejadores de callbacks:
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('vapers', vapers))
    app.add_handler(CommandHandler('candies', candies))
    app.add_handler(CommandHandler('catalogo', send_catalog_image))
    app.add_handler(CommandHandler('weed', weed))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('id', handle_chat_id))

    # Agregar los manejadores de CallbackQueryHandler:
    app.add_handler(CallbackQueryHandler(handle_vaper_selection, pattern='vaper.*'))
    app.add_handler(CallbackQueryHandler(handle_candy_selection, pattern='candy.*'))
    app.add_handler(CallbackQueryHandler(handle_weed_selection, pattern='weed.*'))

    # Respuestas a mensajes:
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Manejo de errores:
    app.add_error_handler(error)

    # Iniciar bot:
    print('Bot iniciado')
    app.run_polling(poll_interval=1, timeout=10)
