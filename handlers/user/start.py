from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from services.news_api import get_news
router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer(
        "Tilni tanlang / Выберите язык / Choose language",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz"),
                    InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
                    InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
                ]
            ]
        )
    )
    
    
    
@router.message(Command("test"))
async def test_news(message: Message):
    news = await get_news("world")
    if not news:
        await message.answer("🚫 Hech qanday yangilik topilmadi.")
        return

    for item in news:
        await message.answer(item)
        