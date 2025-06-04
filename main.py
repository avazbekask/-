from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from handlers.start import start_router
from handlers.menu import menu_router
from handlers.settings import settings_router
from reminder import router as reminder_router
from prayer_times import router as prayer_router
import os

# Инициализация бота
bot = Bot(
    token=os.environ['BOT_TOKEN'],
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

# Подключаем все роутеры
dp.include_router(start_router)
dp.include_router(menu_router)
dp.include_router(settings_router)
dp.include_router(reminder_router)  # Роутер напоминаний
dp.include_router(prayer_router)    # Роутер времени намазов

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())