from telegram import Update
from telegram.ext import ContextTypes

## Manejo de Errores:            
async def error(update: Update, context: ContextTypes):
    print(context.error)
    await update.message.reply_text('Ha ocurrido un error')
