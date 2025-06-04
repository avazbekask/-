from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаем роутер
router = Router()

@router.message(F.text.in_(["🔔 Напоминания", "🔔 Eslatmalar"]))
async def handle_reminders(message: types.Message):
    lang = "ru" if message.text == "🔔 Напоминания" else "uz"

    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Список напоминаний" if lang == "ru" else "📋 Eslatmalar ro'yxati")],
            [KeyboardButton(text="➕ Добавить" if lang == "ru" else "➕ Qo'shish")],
            [KeyboardButton(text="🔙 Назад" if lang == "ru" else "🔙 Orqaga")]
        ],
        resize_keyboard=True
    )

    text = "Управление напоминаниями:" if lang == "ru" else "Eslatmalar boshqaruvi:"
    await message.answer(text, reply_markup=markup)