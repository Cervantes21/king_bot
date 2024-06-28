from telegram import Update
from telegram.ext import ContextTypes, CallbackContext

# Manejo de Errores:            
async def error(update: Update, context: ContextTypes):
    print(context.error)
    await update.message.reply_text('Ha ocurrido un error')
# async def error(update: Update, context: CallbackContext):
#     try:
#         if update.message:
#             await update.message.reply_text('Ha ocurrido un error')
#         elif update.callback_query:
#             await update.callback_query.message.reply_text('Ha ocurrido un error')
#     except Exception as e:
#         print(f"Error while handling error: {e}")
