import asyncio
import logging
import sys
from config import *

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from handlers.start_command import command_start_handler

dp = Dispatcher()

@dp.message(CommandStart())
async def start(m: Message):
    await command_start_handler(m)

async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="log.txt")
    asyncio.run(main())