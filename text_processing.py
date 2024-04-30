from telegram import Update
from telegram.ext import ContextTypes
## Custom Conversation:
def handle_response(text: str, context: ContextTypes, update: Update):
    processed_text = text.lower()
    print(processed_text)
    if '✋' in processed_text or '🖐' in processed_text:
        return 'Hola, ¿Cómo puedo ayudarte? 🖐😋 Puedes decir "Quiero comprar" o enviar un "🚬"'
    elif 'quiero comprar' in processed_text:
        return 'Elige una opción del menú, o inicia con /start'
    
    elif 'gracias' in processed_text:
        return 'Un placer atenderte 😇🤌'
    
    elif 'adios' in processed_text or 'adiós' in processed_text:
        return 'Adiós ✌👽'
    elif 'bye' in processed_text or '👋' in processed_text:
        return 'Adiós ✌👽'
    elif 'catalogo' in processed_text or 'productos' in processed_text:
        return 'Enviando el catálogo...'
    
    elif 'cigarro' in processed_text or ('cigarros' in processed_text and '🚬' in processed_text):
        return '/vapers'

    elif 'dulce' in processed_text or 'chocolate' in processed_text:
        return '/candies'
    elif '🆘' in processed_text or 'help' in processed_text:
        return '¿En que necesitas ayuda? FAQ: 🧐 /help'
    else:
        return 'No te entiendo 😵‍💫 \n favor de presionar: /start' + '\n' + '😌 También puedes interactuar conmigo escribiendo "quiero comprar"' + '\n' '😬 También puedes usar palabras clave del producto que quieres. \n Ejemplo: "cigarro", o usar un Icono "🚬"'
    