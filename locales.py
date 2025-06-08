texts = {
    "uz": {
        "welcome": "Siz o'zbek tilini tanladingiz. Yangiliklarni olish uchun menyudan foydalaning.",
        "choose_category": "Iltimos, kategoriya tanlang:",
        "categories": ["O‘zbekiston🇺🇿", "Jahon🗺", "Iqtisodiyot📊", "Sport🏃🏻‍♂️", "Texnologiya💻"]
    },
    "ru": {
        "welcome": "Вы выбрали русский язык. Используйте меню для получения новостей.",
        "choose_category": "Пожалуйста, выберите категорию:",
        "categories": ["Узбекистан🇺🇿", "Мир🗺", "Общество", "Спорт🏃🏻‍♂️"]
    },
    "en": {
        "welcome": "You selected English. Use the menu to get news.",
        "choose_category": "Please choose a category:",
        "categories": ["POLITICS", "SOCIETY", "BUSINESS📊", "Sport🏃🏻‍♂️", "Technology💻"]
    }
}


def get_mock_news_by_category(category: str, lang: str) -> list[dict]:
    category_map = {
        "Texnologiya": "Technology",
        "Технологии": "Technology",
        "Technology": "Technology",

        "Sport": "Sports",
        "Спорт": "Sports",
        "Sports": "Sports",

        "Iqtisod": "Economy",
        "Экономика": "Economy",
        "Economy": "Economy",
    }

    eng_category = category_map.get(category, "General")

    return [
        {
            "title": f"{eng_category} yangiligi 1",
            "description": f"{eng_category} bo‘yicha birinchi yangilik tavsifi.",
            "url": "https://example.com/1"
        },
        {
            "title": f"{eng_category} yangiligi 2",
            "description": f"{eng_category} bo‘yicha ikkinchi yangilik tavsifi.",
            "url": "https://example.com/2"
        },
        {
            "title": f"{eng_category} yangiligi 3",
            "description": f"{eng_category} bo‘yicha uchinchi yangilik tavsifi.",
            "url": "https://example.com/3"
        },
    ]


CATEGORY_URLS = {
    "uzbekistan": "/news/uzbekistan",
    "world": "/news/world",
    "economy": "/news/economy",
    "sport": "/news/sport",
    "technology": "/news/technology"
}
