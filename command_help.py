from telegram import Update
from telegram.ext import ContextTypes

## Help:
async def help(update: Update, context: ContextTypes):
    await update.message.reply_text("Puedes iniciar la conversación con un Hola, y de ahí ir seleccionando la categoría. Comparte tus dudas: wa.link/7jvf7u 🫡")
  