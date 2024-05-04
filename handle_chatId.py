from telegram import Update
from telegram.ext import CallbackContext

# Función para entregar el id del chat
async def handle_chat_id(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    await update.message.reply_text(f"El ID de este chat es: {chat_id}")
