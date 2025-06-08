# states.py yoki session.py faylida
user_category_selection = {}

def set_user_selected_category(user_id, category):
    user_category_selection[user_id] = category

def get_user_selected_category(user_id):
    return user_category_selection.get(user_id, "technology")  # default
