from telegram import Update
from telegram.ext import ContextTypes

## Help:
async def help(update: Update, context: ContextTypes):
    await update.message.reply_text("Puedes iniciar la conversación con un Hola, y de ahí ir seleccionando la categoría. Comparte tus dudas: wa.link/7jvf7u 🫡")

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
 