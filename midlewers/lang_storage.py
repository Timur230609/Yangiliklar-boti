user_languages = {}

def set_user_language(user_id: int, lang: str):
    user_languages[user_id] = lang

def get_user_language(user_id: int) -> str:
    return user_languages.get(user_id, "uz")
