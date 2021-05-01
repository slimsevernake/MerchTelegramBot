from telebot import types


# Buttons
def show_button():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard="true")
    item_buy = types.KeyboardButton(text="Купить 💣")
    item_basket = types.KeyboardButton(text="Корзина 🧺")
    item_orders = types.KeyboardButton(text="Заказы 📦")
    item_news = types.KeyboardButton(text="Новости 📜")
    item_settings = types.KeyboardButton(text="Настройки ⚙")
    item_help = types.KeyboardButton(text="Помощь 🆘")
    markup.add(item_buy, item_basket, item_orders,
               item_news, item_settings, item_help)
    return markup


def show_inline_button_main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item_bombs = types.InlineKeyboardButton(text="Бомбы 💣",
                                            callback_data="bombs")
    item_lamp_oil = types.InlineKeyboardButton(text="Ламповое масло 💣",
                                               callback_data="lamp_oil")
    item_rope = types.InlineKeyboardButton(text="Веревки 💣",
                                           callback_data="rope")
    markup.add(item_bombs, item_lamp_oil, item_rope)
    return markup