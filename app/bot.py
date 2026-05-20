from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
import os
from dotenv import load_dotenv

from ai import ask_ai
from rag import get_context

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Здравствуйте! Задайте вопрос о компании.")


@dp.message(F.text)
async def chat(message: Message):
    context = get_context(message.text)

    if not context:
        await message.answer("На сайте нет информации по этому вопросу.")
        return

    answer = ask_ai(
        question=message.text,
        context=context
    )

    await message.answer(answer)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
