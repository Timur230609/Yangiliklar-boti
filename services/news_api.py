import aiohttp
import feedparser

RSS_URL = "https://daryo.uz/rss"

async def get_news(category: str, lang: str) -> list[str]:
    # category va lang parametrlari hozir ishlatilmas ekan — saqlab qolamiz
    async with aiohttp.ClientSession() as session:
        async with session.get(RSS_URL) as r:
            if r.status != 200:
                return [f"❗️ RSS olishda xatolik (kod: {r.status})"]
            text = await r.text()

    feed = feedparser.parse(text)
    entries = feed.entries[:5]

    if not entries:
        return ["❗️ Yangiliklar topilmadi."]

    res = []
    for e in entries:
        res.append(f"📰 <b>{e.title}</b>\n🔗 {e.link}")

    return res
