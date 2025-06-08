from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from locales import texts
from midlewers.lang_storage import get_user_language

def category_keyboard(user_id: int) -> ReplyKeyboardMarkup:
    lang = get_user_language(user_id)
    categories = texts.get(lang, texts["uz"])["categories"]

    keyboard = [[KeyboardButton(text=cat) for cat in categories]]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )
