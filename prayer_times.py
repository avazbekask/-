from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()

@router.message(F.text.in_(["🕌 Namoz vaqti", "🕌 Время намаза"]))
async def prayer_times_menu(message: types.Message):
    lang = "uz" if message.text == "🕌 Namoz vaqti" else "ru"

    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📍 Joylashuvni yuborish", request_location=True)],
            [KeyboardButton(text="Toshkent"), KeyboardButton(text="Samarqand")],
            [KeyboardButton(text="🔙 Orqaga" if lang == "uz" else "🔙 Назад")]
        ],
        resize_keyboard=True
    )

    text = (
        "Joylashuvingizni yuboring yoki shaharni tanlang:" 
        if lang == "uz" 
        else "Отправьте локацию или выберите город:"
    )
    await message.answer(text, reply_markup=markup)