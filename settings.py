from aiogram import Router, types
from aiogram import F

settings_router = Router()

@settings_router.message(F.text.in_(["⚙ Настройки", "⚙ Sozlamalar"]))
async def settings_menu(message: types.Message):
    lang = "ru" if message.text == "⚙ Настройки" else "uz"
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🌆 Изменить город" if lang == "ru" else "🌆 Shaharni o‘zgartirish")],
            [types.KeyboardButton(text="🔕 Уведомления" if lang == "ru" else "🔕 Bildirishnomalar")],
            [types.KeyboardButton(text="🔙 Назад" if lang == "ru" else "🔙 Orqaga")]
        ],
        resize_keyboard=True
    )
    text = "Настройки бота:" if lang == "ru" else "Bot sozlamalari:"
    await message.answer(text, reply_markup=keyboard)