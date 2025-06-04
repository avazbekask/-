from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🇷🇺 Русский")],
            [types.KeyboardButton(text="🇺🇿 O'zbekcha")]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите язык:", reply_markup=keyboard)