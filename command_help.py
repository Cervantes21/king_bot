# from telegram import Update
# from telegram.ext import ContextTypes

# ## Help:
# async def command_help(update: Update, context: ContextTypes):
#     url = 'wa.link/7jvf7u'
#     t = f"Puedes iniciar la conversación con un <code><b>Hola</b></code>,\nAhí puedes seleccionar la <u>categoría deseada</u>.\n<b>Comparte tus dudas</b>: {url} 🫡"
#     await update.message.reply_text(t, parse_mode='html')

# # Función para mostrar el menú de Ayuda
# async def sub_menu_help(update: Update, context: CallbackContext):
#     # Crear los botones del submenú Ayuda
#     keyboard = [
#         [InlineKeyboardButton("Preguntas frecuentes", callback_data='faq')],
#         [InlineKeyboardButton("Contacto", callback_data='contact')],
#         [InlineKeyboardButton("Volver al menú principal", callback_data='main_menu')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text("Selecciona una opción de Ayuda:", reply_markup=reply_markup)

from telegram import Update
from telegram.ext import CallbackContext

## Help:
async def command_help(update: Update, context: CallbackContext):
    url = 'wa.link/7jvf7u'
    t = f"Puedes iniciar la conversación con un <code><b>Hola</b></code>,\nAhí puedes seleccionar la <u>categoría deseada</u>.\n<b>Comparte tus dudas</b>: {url} 🫡"
    await update.message.reply_text(t, parse_mode='html')
