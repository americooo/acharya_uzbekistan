from telebot import types
from get_regions import *

def get_name(bot, message, user_data):
    user_id = message.from_user.id
    user_data[user_id]['name'] = message.text  # Store the user's name

    # Ask for birth date in the correct format
    if user_data[user_id]['language'] == 'en':
        bot.send_message(message.chat.id, "Thank you! Now, please enter your birth date in the format DD-MM-YYYY.\n Example: 10-08-1999")
    else:
        bot.send_message(message.chat.id, "Rahmat! Endi tug'ilgan sanangizni Kun-Oy-Yil formatida kiriting.\n Misol uchun: 10-08-1999")

def get_birth_date(bot, message, user_data):
    user_id = message.from_user.id
    birth_date = message.text  # Get the entered birth date

    # Validate the birth date format
    try:
        day, month, year = map(int, birth_date.split('-'))
        user_data[user_id]['birth_date'] = birth_date

        # Ask for phone number after birth date
        if user_data[user_id]['language'] == 'en':
            bot.send_message(message.chat.id, "Thank you! ")
        else:
            bot.send_message(message.chat.id, "Rahmat!.")

        # Button for sharing phone number
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button = types.KeyboardButton(
            'Send phone number' if user_data[user_id]['language'] == 'en' else 'Telefon raqamni yuboring',
            request_contact=True
        )
        markup.add(button)
        bot.send_message(
            message.chat.id,
            'Please share your phone number:' if user_data[user_id]['language'] == 'en' else 'Iltimos, telefon raqamingizni yuboring:',
            reply_markup=markup
        )
    except ValueError:
        if user_data[user_id]['language'] == 'en':
            bot.send_message(message.chat.id, "Invalid date format. Please enter the date in the format Date-Month-Year.")
        else:
            bot.send_message(message.chat.id, "Sana formati noto‘g‘ri. Iltimos, sanani Kun-Oy-Yil formatida kiriting.")

def handle_phone_number(bot, message, user_data):
    user_id = message.from_user.id

    # Ensure user_data entry exists
    if user_id not in user_data:
        user_data[user_id] = {}

    # Handle phone number input
    if message.content_type == 'contact':
        phone_number = message.contact.phone_number
    else:  # Handle manual phone number input
        phone_number = message.text

    user_data[user_id]['phone_number'] = phone_number

    # Ask for region selection
    language = user_data[user_id].get('language', 'en')
    bot.send_message(
        message.chat.id,
        "Please select your region:" if language == 'en' else "Iltimos, viloyatni tanlang tanlang:", reply_markup=generate_region_keyboard)
