import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN, ADMIN_IDS
from handlers.user.start import router as start_router
from handlers.user.language import router as language_router
from handlers.user.category import router as category_router

# Bot ishga tushganda adminlarga xabar yuborish
async def on_start(bot: Bot):
    for admin_id in ADMIN_IDS:
        try:
            await bot.send_message(admin_id, "✅ Bot ishga tushdi!")
        except Exception as e:
            logging.exception(f"Adminga xabar yuborishda xatolik: {e}")

# Bot to'xtaganda adminlarga xabar yuborish
async def on_shutdown(bot: Bot):
    for admin_id in ADMIN_IDS:
        try:
            await bot.send_message(admin_id, "❌ Bot ishdan to‘xtadi.")
        except Exception as e:
            logging.exception(f"Adminga xabar yuborishda xatolik: {e}")


async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode="HTML")
    )
    dp = Dispatcher(storage=MemoryStorage())

    # Routerlarni qo‘shamiz
    dp.include_routers(
        start_router,
        language_router,
        category_router,
        # subcategory_router olib tashlandi, chunki endi ishlatilmaydi
    )

    dp.startup.register(on_start)
    dp.shutdown.register(on_shutdown)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
