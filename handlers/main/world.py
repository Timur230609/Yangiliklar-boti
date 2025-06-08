import requests

NEWS_API_KEY = "9cedc975f1c2458b864f497aaac8dcf9" 

def get_news(category: str, subcategory: str):
    if subcategory == "Dunyo":
        url = f"https://newsapi.org/v2/top-headlines?language=en&category={category.lower()}&apiKey={NEWS_API_KEY}"
    elif subcategory == "O‘zbekiston":
        # NewsAPI o‘zbek tilini to‘liq qo‘llamaydi, shuning uchun regionga mos proxy variant kerak
        url = f"https://newsapi.org/v2/top-headlines?country=uz&category={category.lower()}&apiKey={NEWS_API_KEY}"
    else:
        return ["Subkategoriya noto‘g‘ri"]

    response = requests.get(url)
    data = response.json()

    if data["status"] != "ok":
        return ["Yangiliklarni yuklashda xatolik"]

    news_list = []
    for article in data["articles"][:5]:  # Faqat 5 ta yangilik
        news_list.append(f"📰 {article['title']}\n{article['url']}")

    return news_list
