from telebot import types

def start(bot, message):
    user_first_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"Hello {user_first_name}! ")

    # Inline keyboard for language selection
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("English🇺🇸", callback_data="lang_en"))
    markup.add(types.InlineKeyboardButton("O'zbek🇺🇿", callback_data="lang_uz"))
    bot.send_message(message.chat.id, "Choose your language:", reply_markup=markup)

def handle_language_selection(bot, call, user_data):
    user_id = call.from_user.id
    lang_code = call.data.split("_")[1]  # Get language code
    user_data[user_id] = {"language": lang_code}  # Store selected language

    # Send message in selected language
    if lang_code == 'en':
        bot.send_message(call.message.chat.id, "Please enter your name.")
    elif lang_code == 'uz':
        bot.send_message(call.message.chat.id, "Iltimos, ism va familiyangizni kiriting.")
