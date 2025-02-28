from telebot import TeleBot
from sections import get_sections_keyboard  # Import keyboard generation function

def generate_district_keyboard(bot: TeleBot, user_data: dict):
    @bot.callback_query_handler(func=lambda call: call.data.startswith("district_"))
    def get_district(call):
        district = call.data.split("_")[1]  # Extract selected district
        user_id = call.from_user.id
        user_data[user_id]['district'] = district  # Store district

        language = user_data[user_id].get('language', 'en')
        bot.send_message(
            call.message.chat.id,
            f"District set to {district}. Now, please choose your subject." if language == 'en' else f"Tuman {district} sifatida belgilandi. Endi yo'nalishingizni tanlang.",
            reply_markup=get_sections_keyboard(language)
        )
