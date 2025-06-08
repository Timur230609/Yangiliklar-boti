from locales import texts
from aiogram import Router, F
from aiogram.types import Message
from midlewers.lang_storage import get_user_language
from services.news_api import get_news

router = Router()

# Mapping (kategoriya matni -> API nomi)
category_map = {
    "texnologiya": "technology",
    "технологии": "technology",
    "technology": "technology",

    "sport": "sport",
    "спорт": "sport",
    "sports": "sport",

    "iqtisodiyot": "economy",
    "экономика": "economy",
    "economy": "economy",

    "jahon": "world",
    "мир": "world",
    "world": "world",

    "o‘zbekiston": "uzbekistan",
    "узбекистан": "uzbekistan",
    "uzbekistan": "uzbekistan"
}

@router.message(F.text.lower().in_(category_map.keys()))
async def send_news(message: Message):
    user_input = message.text.lower()
    lang = get_user_language(message.from_user.id)

    api_category = category_map.get(user_input)
    if not api_category:
        await message.answer("❗️ Kategoriya aniqlanmadi.")
        return

    news_list = await get_news(api_category, lang)  # Tilni ham uzatamiz!

    if not news_list or (len(news_list) == 1 and news_list[0].startswith("❗️")):
        await message.answer("❗️ Yangiliklar topilmadi.")
        return

    for news in news_list:
        await message.answer(
            news,
            disable_web_page_preview=True,
            parse_mode="HTML"
        )
    