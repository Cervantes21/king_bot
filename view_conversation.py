import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('conversations.db')
cursor = conn.cursor()

# Consultar las conversaciones
cursor.execute('SELECT * FROM conversations')
conversations = cursor.fetchall()

# Mostrar las conversaciones
for conversation in conversations:
    user_name, user_id, date, message, chat_id, message_id, response = conversation
    print(f'User Name: {user_name}')
    print(f'User ID: {user_id}')
    print(f'Date: {date}')
    print(f'Message: {message}')
    print(f'Chat ID: {chat_id}')
    print(f'Message ID: {message_id}')
    print(f'Response: {response}')
    print('-' * 50)

# Cerrar la conexión a la base de datos
conn.close()

