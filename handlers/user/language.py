from locales import texts
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.default import category_keyboard
from midlewers.lang_storage import set_user_language

router = Router()

@router.callback_query(F.data.startswith("lang_"))
async def set_language(callback: CallbackQuery):
    lang_code = callback.data.split("_")[1]

    # Foydalanuvchi tanlagan tilni saqlaymiz
    set_user_language(callback.from_user.id, lang_code)

    # Tilga mos matnlarni olish (agar topilmasa, "uz" tilini olamiz)
    lang_texts = texts.get(lang_code, texts["uz"])

    # Xush kelibsiz matnini o‘zgartiramiz (edit_text bilan)
    await callback.message.edit_text(lang_texts.get("welcome", "Xush kelibsiz!"))

    # Kategoriya tanlash xabari va klaviaturasi
    await callback.message.answer(
        lang_texts.get("choose_category", "Iltimos, kategoriya tanlang:"),
        reply_markup=category_keyboard(callback.from_user.id)
    )

    # Callbackni tasdiqlaymiz (hech qanday ogohlantirish chiqmasligi uchun)
    await callback.answer()
