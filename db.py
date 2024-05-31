from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging
import psycopg2
from psycopg2.extras import Json
from dotenv import load_dotenv
import os

# Configuración del registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Cargar las variables de entorno
load_dotenv()

# Datos de conexión a la base de datos desde variables de entorno
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Función para conectar a la base de datos
def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

# Comando /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('¡Hola! Soy tu bot de Telegram. ¿Cómo puedo ayudarte hoy?')

# Manejar mensajes
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    message_text = update.message.text

    # Conectar a la base de datos
    conn = connect_db()
    cur = conn.cursor()

    # Verificar si el usuario ya tiene conversaciones guardadas
    cur.execute("SELECT messages FROM conversations WHERE user_id = %s", (user_id,))
    result = cur.fetchone()

    if result:
        # Agregar el mensaje a las conversaciones existentes
        messages = result[0]
        messages.append(message_text)
        cur.execute("UPDATE conversations SET messages = %s WHERE user_id = %s", (Json(messages), user_id))
    else:
        # Crear una nueva entrada para el usuario
        cur.execute("INSERT INTO conversations (user_id, messages) VALUES (%s, %s)", (user_id, Json([message_text])))

    # Confirmar la transacción y cerrar la conexión
    conn.commit()
    cur.close()
    conn.close()

    # Responder al usuario
    await update.message.reply_text('He guardado tu mensaje.')

def main() -> None:
    # Token del bot de Telegram
    token = os.getenv('TOKEN')
    
    # Crear la aplicación
    application = Application.builder().token(token).build()

    # Agregar manejadores al dispatcher
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
