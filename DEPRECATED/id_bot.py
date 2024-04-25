import asyncio
from telegram import Bot

async def get_chat_id():
    bot = Bot(token = '7030212913:AAEvSDODlRFtKApMGEWyf8WiCj7pkr-H40s')
    me = await bot.get_me()
    chat_id = me.id
    return chat_id

async def main():
    chat_id = await get_chat_id()
    print("Chat ID:", chat_id)

if __name__ == "__main__":
    asyncio.run(main())
