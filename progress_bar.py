import os
from dotenv import load_dotenv

import time

import telebot

# Constantes:
load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=["bar"])
def cmd_bar(m):
    inf = "✔ <b>BOT INICIADO</b>"
    bot.send_message(m.chat,id, inf, parse_mode="HTML")

@bot.message_handler(commands=["show"])
def show_bar(m):
    cid = m.chat.id
    mid = bar(0, 'Iniciando...', cid)
    time.sleep(3)
    bar(10, "Preparando el carrito 🛒", cid, mid)
    time.sleep(3)
    bar(15, "Estamos revisando los datos 🔍", cid, mid)
    time.sleep(4)
    bar(45, "Espera un poco más, estamos revisando la información ⚙", cid, mid)
    time.sleep(5)
    bar(100, "Información completada ☑", cid, mid)


def cursor_up(n=1):
    '''Sube el cursos de la terminal n lineas'''
    print(f'\33[{n}A', end='')

def bar(per, text="", cid=None, mid=None, terminal=True):
    t, no, si = ('█','⬜','⬛')  # terminal, Telegram vacío, Telegram lleno
    if terminal:
        #Colors
        white = "\33[1;37m"
        yw = "\33[1;33m"
        gray = "\33[0;37m"
        gray2 = "\33[0;90m"
        width = os.get_terminal_size().columns - 7
        square_on = per * width // 100
        square_off = width - square_on
        
        terminal_bar = f'\33[K{white}|{yw}{t*square_on}{gray2}{t*square_off}{white}| {per:>3}%{gray}'
        text_terminal = f'\33[K{yw} {text}\n{terminal_bar}'
        print(text_terminal)
        if per < 100:
            cursor_up(2)

    # Telegram
    if cid:
        square_on = per // 10
        square_off = 10 - square_on
        # Barra de progreso:
        bar_telegram = si*square_on + no*square_off
        msg_telegram = f'{text}\n{bar_telegram} <code>{per:>3}%</code>'
        if not mid:
            msg = bot.send_message(cid, msg_telegram, parse_mode="html")
            # Capturamos el message_id
            return msg.message_id
        else:
            # Si el mensaje es inferior al 100%
            if per < 100:
                bot.edit_message_text(msg_telegram, cid, mid, parse_mode="html")
            # Si ha llegado al 100&
            elif per == 100:
                bot.edit_message_text(msg_telegram, cid, mid, parse_mode="html")
                time.sleep(3)
                bot.delete_message(cid, mid)
                return
            else:
                bot.delete_message(cid, mid)
                return 'Ha ocurrido un error.'

if __name__ == '__main__':
    bot.infinity_polling(timeout=60)        
