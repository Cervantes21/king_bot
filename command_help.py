from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, ContextTypes, CallbackQueryHandler

# Comando de ayuda
async def command_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = 'wa.link/7jvf7u'
    t = f"Puedes iniciar la conversación con un <code><b>Hola</b></code>,\nAhí puedes seleccionar la <u>categoría deseada</u>.\n<b>Comparte tus dudas</b>: {url} 🫡"
    if update.message:
        await update.message.reply_text(t, parse_mode='html')
    elif update.callback_query:
        await update.callback_query.message.edit_text(text=t, parse_mode='html')

# Función para mostrar el submenú de Ayuda
async def sub_menu_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Crear los botones del submenú Ayuda
    keyboard = [
        [InlineKeyboardButton("Preguntas frecuentes", callback_data='faq')],
        [InlineKeyboardButton("Contacto", callback_data='contact')],
        [InlineKeyboardButton("Volver al menú principal", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    m = "Selecciona una opción de Ayuda:"
    if update.message:
        await update.message.reply_text(m, reply_markup=reply_markup, parse_mode='html')
    elif update.callback_query:
        await update.callback_query.message.edit_text(m, reply_markup=reply_markup, parse_mode='html')

# Función para manejar las opciones del menú
async def menu_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'faq':
        await command_help(query, context)
    elif query.data == 'contact':
        await query.edit_message_text(text="Puedes contactarnos a través de: https://t.me/kings_boulevard")
    elif query.data == 'main_menu':
        from start import start
        await start(query, context)
