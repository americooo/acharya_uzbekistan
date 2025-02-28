from telebot import TeleBot

def get_sections_keyboard(bot: TeleBot, user_data: dict, admin_ids: list):
    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def section_choice(message):
        user_id = message.from_user.id

        # Validate all required data before proceeding
        required_keys = ['phone_number', 'region', 'district']
        if user_id in user_data and all(key in user_data[user_id] for key in required_keys):
            chosen_section = message.text
            user_data[user_id]['chosen_section'] = chosen_section  # Store section

            # Confirmation message based on language
            language = user_data[user_id].get('language', 'en')
            bot.send_message(
                message.chat.id,
                "Thank you for providing your details! You will receive updates soon." if language == 'en' else "Ma'lumotlaringiz uchun rahmat! Tez orada yangiliklarni olasiz."
            )

            # Prepare and send data to admins
            admin_message = (
                f"🆕 New Registration:\n\n"
                f"📄 Name: {user_data[user_id].get('name', 'N/A')}\n"
                f"🎂 Birth Date: {user_data[user_id].get('birth_date', 'N/A')}\n"
                f"📞 Phone Number: {user_data[user_id]['phone_number']}\n"
                f"📍 Region: {user_data[user_id]['region']}\n"
                f"🌍 District: {user_data[user_id]['district']}\n"
                f"📝 Section: {user_data[user_id]['chosen_section']}"
            )

            # Send the registration data to admins
            for admin_id in admin_ids:
                bot.send_message(admin_id, admin_message)
        else:
            bot.send_message(
                message.chat.id,
                "Incomplete data. Please complete the previous steps." if user_data[user_id].get('language') == 'en' else "Ma'lumotlar to'liq emas. Iltimos, avvalgi qadamlarni yakunlang."
            )
