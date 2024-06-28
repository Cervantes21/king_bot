from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

## Crear menú de bienvenida:
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Crear los botones
    keyboard = [
        [InlineKeyboardButton("Vapers 🚬", callback_data='vapers_menu')],
        [InlineKeyboardButton("Dulces con THC 🍫🍭", callback_data='candies')],
        [InlineKeyboardButton("Cultivos 🌱", callback_data='weed')],
        [InlineKeyboardButton("Ayuda 😟", callback_data='help')],
        [InlineKeyboardButton("CERRAR ❌", callback_data='close')]
    ]
    # Adjuntar los botones al mensaje de bienvenida
    reply_markup = InlineKeyboardMarkup(keyboard)
    m = "Hola, soy un <b>King</b>. ¿En qué puedo ayudarte?"+"\n"+"<code>Elige una opción:</code>"

    if update.message:
        await update.message.reply_text(m, reply_markup=reply_markup, parse_mode='html')
    elif update.callback_query:
        await update.callback_query.message.edit_text(m, reply_markup=reply_markup, parse_mode='html')

async def handler_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    if data == 'vapers_menu':
        from select_vaper import selected_vaper
        await selected_vaper(update, context)
    elif data == 'candies':
        from select_candy import candies
        await candies(update, context)
    elif data == 'weed':
        from select_w import weed
        await weed(update, context)
    elif data == 'help':
        from command_help import sub_menu_help
        await sub_menu_help(update, context)
    else:
        await start(update, context)

        


