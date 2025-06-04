from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F

menu_router = Router()

# Главное меню (русский)
@menu_router.message(F.text == "🇷🇺 Русский")
async def russian_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📋 Меню")],
            [types.KeyboardButton(text="🕌 Время намаза")],
            [types.KeyboardButton(text="🔔 Напоминания")],
            [types.KeyboardButton(text="⚙ Настройки")]
        ],
        resize_keyboard=True,
        persistent=True  # Кнопки не исчезают после перезапуска
    )
    await message.answer("Главное меню:", reply_markup=keyboard)

# Главное меню (узбекский)
@menu_router.message(F.text == "🇺🇿 O'zbekcha")
async def uzbek_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📋 Menu")],
            [types.KeyboardButton(text="🕌 Namoz vaqti")],
            [types.KeyboardButton(text="🔔 Eslatmalar")],
            [types.KeyboardButton(text="⚙ Sozlamalar")]
        ],
        resize_keyboard=True,
        persistent=True
    )
    await message.answer("Asosiy menyu:", reply_markup=keyboard)

# Кнопка "Назад" (возврат в главное меню)
@menu_router.message(F.text.in_(["🔙 Назад", "🔙 Orqaga"]))
async def back_to_menu(message: types.Message):
    lang = "ru" if message.text == "🔙 Назад" else "uz"
    await (russian_menu(message) if lang == "ru" else uzbek_menu(message))