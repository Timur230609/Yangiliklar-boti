from aiogram import Router, F
from aiogram.types import Message
from midlewers.lang_storage import get_user_language
from locales import texts
from services.news_api import get_news

router = Router()

# Har bir til uchun barcha mavjud kategoriyalar
ALL_CATEGORIES = texts["uz"]["categories"] + texts["ru"]["categories"] + texts["en"]["categories"]

# Kategoriya matnlarini API nomiga mapping qilish
CATEGORY_MAP = {
    # O'zbekcha
    "O‘zbekiston🇺🇿": ("uzbekistan", "uz"),
    "Jahon🗺": ("world", "uz"),
    "Iqtisodiyot📊": ("economy", "uz"),
    "Sport🏃🏻‍♂️": ("sport", "uz"),
    "Texnologiya💻": ("technology", "uz"),

    # Ruscha
    "Узбекистан🇺🇿": ("uzbekistan", "ru"),
    "Мир🗺": ("world", "ru"),
    "Общество": ("society", "ru"),
    "Спорт🏃🏻‍♂️": ("sport", "ru"),

    # Inglizcha
    "POLITICS": ("politics", "en"),
    "SOCIETY": ("society", "en"),
    "BUSINESS📊": ("business", "en"),
    "Sport🏃🏻‍♂️": ("sport", "en"),
    "Technology💻": ("technology", "en"),
}


@router.message(F.text.in_(ALL_CATEGORIES))
async def show_news(message: Message):
    user_id = message.from_user.id
    lang = get_user_language(user_id)
    category_text = message.text.strip()

    mapped = CATEGORY_MAP.get(category_text)
    if not mapped:
        await message.answer("❗️Kechirasiz, bu kategoriya topilmadi.")
        return

    api_category, lang_code = mapped

    # Yangiliklarni olish
    news_list = await get_news(api_category, lang_code)

    # Xatolik yoki yangiliklar yo‘qligi haqida xabar bo‘lsa
    if not news_list or not isinstance(news_list, list):
        await message.answer("❗️Yangiliklarni yuklashda muammo yuz berdi.")
        return

    for news in news_list:
        await message.answer(news)
