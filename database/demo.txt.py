
# # Step 1: Function to start gathering birth date details
# def ask_birth_year(message):
#     user_id = message.from_user.id
#     # Ask for the birth year
#     if user_data[user_id]['language'] == 'en':
#         bot.send_message(message.chat.id, "Please enter your birth year (e.g., 2000).")
#     else:
#         bot.send_message(message.chat.id, "Tug'ilgan yilingizni kiriting (masalan, 2000).")
#     bot.register_next_step_handler(message, get_birth_year)
#
#
# # Step 2: Get the birth year
# def get_birth_year(message):
#     user_id = message.from_user.id
#     birth_year = message.text
#
#     if birth_year.isdigit() and 1900 <= int(birth_year) <= 2100:  # Validate year input
#         user_data[user_id]['birth_year'] = birth_year  # Store birth year
#
#         # Ask for the birth month
#         if user_data[user_id]['language'] == 'en':
#             bot.send_message(message.chat.id, "Thank you! Now, please enter your birth month (1-12).")
#         else:
#             bot.send_message(message.chat.id, "Rahmat! Endi tug'ilgan oyingizni kiriting (1-12).")
#
#         bot.register_next_step_handler(message, get_birth_month)  # Proceed to get the birth month
#     else:
#         # Retry if input is invalid
#         bot.send_message(message.chat.id, "Invalid year format. Please enter a valid birth year (e.g., 2000).")
#         bot.register_next_step_handler(message, get_birth_year)
#
#
# # Step 3: Get the birth month
# def get_birth_month(message):
#     user_id = message.from_user.id
#     birth_month = message.text
#
#     if birth_month.isdigit() and 1 <= int(birth_month) <= 12:  # Validate month input
#         user_data[user_id]['birth_month'] = birth_month  # Store birth month
#
#         # Ask for the birth day
#         if user_data[user_id]['language'] == 'en':
#             bot.send_message(message.chat.id, "Thanks! Now, please enter your birth day (1-31).")
#         else:
#             bot.send_message(message.chat.id, "Rahmat! Endi tug'ilgan kuningizni kiriting (1-31).")
#
#         bot.register_next_step_handler(message, get_birth_day)  # Proceed to get the birth day
#     else:
#         bot.send_message(message.chat.id, "Invalid month format. Please enter a valid birth month (1-12).")
#         bot.register_next_step_handler(message, get_birth_month)  # Retry if invalid input
#
#
# # Step 4: Get the birth day and display the full date
# def get_birth_day(message):
#     user_id = message.from_user.id
#     birth_day = message.text
#
#     if birth_day.isdigit() and 1 <= int(birth_day) <= 31:  # Validate day input
#         user_data[user_id]['birth_day'] = birth_day  # Store birth day
#
#         # Concatenate day, month, year to create the full birth date
#         full_birthday = f"{user_data[user_id]['birth_day']}-{user_data[user_id]['birth_month']}-{user_data[user_id]['birth_year']}"
#         user_data[user_id]['birthday'] = full_birthday  # Store the full birth date
#
#         # Confirmation message
#         if user_data[user_id]['language'] == 'en':
#             bot.send_message(message.chat.id,
#                              f"Thank you! Your birth date is {full_birthday}. Now, please choose your region.")
#         else:
#             bot.send_message(message.chat.id,
#                              f"Rahmat! Sizning tug'ilgan sanangiz {full_birthday}. Endi mintaqangizni tanlang.")
#
#         # Inline keyboard for region choices (same as before)
#         markup = types.InlineKeyboardMarkup()
#         regions = ['Termiz', 'Surxondaryo', 'Farg`ona', 'Navoiy', 'Bukhara', 'Qashqadaryo', 'Xorazm', 'Jizzax', 'Nukus',
#                    'Samarqand', 'Sirdaryo', 'Toshkent shahri']
#         for region in regions:
#             markup.add(types.InlineKeyboardButton(region, callback_data=f"region_{region}"))
#         bot.send_message(message.chat.id, 'Please choose your region:' if user_data[user_id][
#                                                                               'language'] == 'en' else 'Iltimos, viloyatni tanlang 👇:',
#                          reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, "Invalid day format. Please enter a valid birth day (1-31).")
#         bot.register_next_step_handler(message, get_birth_day)  # Retry if invalid input
#
#
# # Call this function to initiate birth date input after language selection or any suitable point
# @bot.message_handler(commands=['start'])
# def start(message):
#     user_first_name = message.from_user.first_name
#     bot.send_message(message.chat.id, f"Hello {user_first_name}! Please choose your language.")
#
#     # Inline keyboard for language selection
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("English🇺🇸", callback_data="lang_en"))
#     markup.add(types.InlineKeyboardButton("O'zbek🇺🇿", callback_data="lang_uz"))
#     bot.send_message(message.chat.id, "Choose your language:", reply_markup=markup)
#
#
# # Trigger ask_birth_year function as the next step after language selection
# @bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
# def handle_language_selection(call):
#     user_id = call.from_user.id
#     lang_code = call.data.split("_")[1]  # Get language code
#     user_data[user_id] = {"language": lang_code}  # Store selected language
#     ask_birth_year(call.message)

import telebot
from telebot import types

API_TOKEN = '6445543196:AAHG9mjlmC9AbhO8xStWz6Pws6Yg0k75WI4'
ADMIN_ID1 = '1861209145'
ADMIN_ID2 = '5313781530'

user_data = {}  # Dictionary to store user data (language, name, phone number, region, district, and section)

bot = telebot.TeleBot(API_TOKEN)

# Define districts for each region
districts_by_region = {
    "Termiz": ["Angor tumani", "Bandixon tumani", "Boysun tumani", "Denov tumani", "Jarqorgon tumani","Muzrabot tumani", "Oltinsoy tumani", "Qiziriq tumani", "Qumqorgon tumani", "Sariosiyo tumani", "Sherobot tumani", "Shorchi tumani", "Uzun tumani"],
    "Surxondaryo": ["Angor tumani", "Bandixon tumani", "Boysun tumani","Denov tumani","Jarqorgon tumani","Muzrabot tumani","Oltinsoy tumani","Qiziriq tumani","Qumqorgon tumani","Sariosiyo tumani","Sherobot tumani","Shorchi tumani","Uzun tumani"],
    "Fargona": ["Beshariq tumani","Bogdod tumani","Buvayda tumani	","Dangara tumani","Fargona shahri","Fargona tumani","Furqat tumani","Margilon shahri","Ozbekiston tumani","Oltiariq tumani","Qoqon shahri","Qoshtepa tumani","Quva tumani","Quvasoy shahri","Rishton tumani","Sox tumani","Toshloq tumani","Uchkoprik tumani","Yozyovon tumani"],
    "Navoiy": ["Konimex tumani","Navbahor tumani","Navoiy tumani","Nurota tumani","Qiziltepa tumani","Tomdi tumani","Uchquduq tumani","Xatirchi tumani"],
    "Bukhara": ["Buxoro tumani","Gijduvon tumani ","Jondor tumani","Kogon tumani ","Olot tumani","Peshku tumani","Qorakol tumani","Qorovulbozor tumani","Romitan tumani","Shofirkon tumani","Vobkent tumani"],
    "Qashqadaryo": ["Chiroqchi tumani","Dehqonobod tumani","Gʻuzor tumani ","Kasbi tumani ","Kitob tumani","Koson tumani","Mirishkor tumani","Muborak tumani","Nishon tumani","Qamashi tumani","Qarshi tumani","Shahrisabz tumani","Yakkabog tumani"],
    "Xorazm": ["Bogot tumani","Gurlan tumani","Hazorasp tumani","Qoshkopir tumani","Shovot tumani","Urganch tumani","Xiva tumani","Xonqa tumani ","Yangiariq tumani","Yangibozor tumani"],
    "Jizzax": ["Arnasoy tumani","Baxmal tumani","Dostlik tumani","Forish tumani ","Gallaorol tumani "," Jizzax tumani","Mirzachol tumani ","Paxtakor tumani ","Sharof Rashidov tumani ","Yangiobod tumani","Zafarobod tumani","Zarbdor tumani","Zomin tumani"],
    "Nukus": ["Amudaryo tumani","Beruniy tumani","Chimboy tumani","Ellikqala tumani","Kegeyli tumani","Moynoq tumani","Nukus shahri","Nukus tumani","Qonlikol tumani","Qorauzaq tumani","Qungirot tumani","Shumanay tumani","Taxiatosh shahri","Taxtakopir tumani","Tortkol tumani","Xojayli tumani"],
    "Samarqand": ["	Bulungur tumani","Ishtixon tumani","Jomboy tumani","Kattaqorgon shahri","Kattaqorgon tumani","Narpay tumani","Nurobod tumani","Oqdaryo tumani","Past dargom tumani","Paxtachi tumani","Poyariq tumani","Qoshrabot tumani","Samarqand shahri","Samarqand tumani","Toyloq tumani","Urgut tumani"],
    "Sirdaryo": ["Boyovut tumani","Guliston tumani","Mirzaobod tumani","Oqoltin tumani","Sayxunobod tumani","Sardoba tumani","Sirdaryo tumani","Xovos tumani"],
    "Toshkent shahar": ["Bektemir tumani","Chilonzor tumani","Mirobod tumani","Mirzo Ulugbek tumani","Olmazor tumani","Sergeli tumani","Shayhontohur tumani","Uchtepa tumani","Yakkasaroy tumani","Yashnaobod tumani","Yunusobod tumani"],
    #   # Add other regions and districts...
}

# Admin command
@bot.message_handler(commands=['admin'])
def admins(message):
    bot.send_message(message.chat.id, f"👮‍ Universitet Ma'muriyati - @Acharya_support \n\n👨‍💻 Bot Ma'muriyati - @americo_444")

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    user_first_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"Hello {user_first_name}! Please choose your language.")

    # Inline keyboard for language selection
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("English🇺🇸", callback_data="lang_en"))
    markup.add(types.InlineKeyboardButton("O'zbek🇺🇿", callback_data="lang_uz"))
    bot.send_message(message.chat.id, "Choose your language:", reply_markup=markup)

# Handle language selection
@bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
def handle_language_selection(call):
    user_id = call.from_user.id
    lang_code = call.data.split("_")[1]  # Get language code
    user_data[user_id] = {"language": lang_code}  # Store selected language

    # Send message in selected language
    if lang_code == 'en':
        bot.send_message(call.message.chat.id, "Please enter your name.")
    elif lang_code == 'uz':
        bot.send_message(call.message.chat.id, "Iltimos, ism va familiyangizni kiriting  kiriting.")


# Handle user's name
@bot.message_handler(
    func=lambda message: message.from_user.id in user_data and 'name' not in user_data[message.from_user.id])
def get_name(message):
    user_id = message.from_user.id
    user_data[user_id]['name'] = message.text  # Store the user's name

    # Ask for birth date in the correct format
    if user_data[user_id]['language'] == 'en':
        bot.send_message(message.chat.id, "Thank you! Now, please enter your birth date in the format DD-MM-YYYY.")
    else:
        bot.send_message(message.chat.id, "Rahmat! Endi tug'ilgan sanangizni Kun-Oy-Yil formatida kiriting.")






# Handle user's birth date
@bot.message_handler(
    func=lambda message: message.from_user.id in user_data and 'birth_date' not in user_data[message.from_user.id])
def get_birth_date(message):
    user_id = message.from_user.id
    birth_date = message.text  # Get the entered birth date

    # Validate the birth date format
    try:
        day, month, year = map(int, birth_date.split('-'))
        # Store the date if the format is correct
        user_data[user_id]['birth_date'] = birth_date

        # Ask for phone number after birth date
        if user_data[user_id]['language'] == 'en':
            bot.send_message(message.chat.id, "Thank you! Now, please send your phone number.")
        else:
            bot.send_message(message.chat.id, "Rahmat! Endi telefon raqamingizni yuboring.")

        # Button for sharing phone number
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button = types.KeyboardButton('Send phone number' if user_data[user_id]['language'] == 'en' else 'Telefon raqamni yuboring',request_contact=True
        )
        markup.add(button)
        bot.send_message(message.chat.id, 'Please share your phone number:' if user_data[user_id]['language'] == 'en' else 'Iltimos, telefon raqamingizni yuboring:',reply_markup=markup)

    except ValueError:
        # If date format is incorrect, ask again
        if user_data[user_id]['language'] == 'en':
            bot.send_message(message.chat.id, "Invalid date format. Please enter the date in the format Date-Month-Year.")
        else:
            bot.send_message(message.chat.id, "Sana formati noto‘g‘ri. Iltimos, sanani Kun-Oy-Yil formatida kiriting.")


# Handle contact message (phone number)
@bot.message_handler(content_types=['contact'])
def get_phone_number(message):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        user_data[user_id]['phone_number'] = phone_number  # Store phone number for the user

        # Send confirmation based on language preference
        if user_data[user_id]['language'] == 'en':
            bot.send_message(message.chat.id, "Thank you for sharing your phone number! Now, please choose your region.")
        else:
            bot.send_message(message.chat.id, "Telefon raqamingiz uchun rahmat! Endi mintaqangizni tanlang.")

        # Inline keyboard for region choices
        markup = types.InlineKeyboardMarkup()
        regions = ['Termiz', 'Surxondaryo', 'Fargona', 'Navoiy', 'Bukhara', 'Qashqadaryo', 'Xorazm', 'Jizzax', 'Nukus', 'Samarqand', 'Sirdaryo', 'Toshkent shahri']
        for region in regions:
            markup.add(types.InlineKeyboardButton(region, callback_data=f"region_{region}"))
        bot.send_message(message.chat.id, 'Please choose your region:' if user_data[user_id]['language'] == 'en' else 'Iltimos, viloyatni  tanlang 👇:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Please use the button to share your phone number.' if user_data[user_id]['language'] == 'en' else 'Telefon raqamni yuborish tugmasidan foydalaning.')

# Handle region selection and display district options
@bot.callback_query_handler(func=lambda call: call.data.startswith("region_"))
def get_region(call):
    user_id = call.from_user.id
    region = call.data.split("_")[1]  # Get selected region
    user_data[user_id]['region'] = region  # Store the chosen region

    # Send district selection message
    if region in districts_by_region:
        if user_data[user_id]['language'] == 'en':
            bot.send_message(call.message.chat.id, f"Region set to {region}. Now, please choose your district.")
        else:
            bot.send_message(call.message.chat.id, f"Viloyat {region} sifatida belgilandi. Endi tumaningizni tanlang.")

        # Inline keyboard for district choices
        markup = types.InlineKeyboardMarkup()
        for district in districts_by_region[region]:
            markup.add(types.InlineKeyboardButton(district, callback_data=f"district_{district}"))
        bot.send_message(call.message.chat.id, "Please select your district:" if user_data[user_id]['language'] == 'en' else "Iltimos, tumaningizni tanlang 👇:", reply_markup=markup)

# Handle district selection
@bot.callback_query_handler(func=lambda call: call.data.startswith("district_"))
def get_district(call):
    user_id = call.from_user.id
    district = call.data.split("_")[1]  # Get selected district
    user_data[user_id]['district'] = district  # Store the chosen district

    # Send confirmation message based on language preference
    if user_data[user_id]['language'] == 'en':
        bot.send_message(call.message.chat.id, f"District set to {district}. Now, please choose your subject.")
    else:
        bot.send_message(call.message.chat.id, f"Tuman {district} sifatida belgilandi. Endi yo'nalishingizni tanlang.")

    # Create keyboard for section choices
    sections = ['Software Engineer', 'Cloud Computing and Security', 'Artificial Intelligence and Machine Learning', 'Computer Science & Engineering', 'Data Science', 'Information Technology', 'Data Analytics', 'Full Stack Development', 'UI & UX Design']
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for section in sections:
        markup.add(types.KeyboardButton(section))
    bot.send_message(call.message.chat.id, 'Please choose a subject:' if user_data[user_id]['language'] == 'en' else 'Iltimos, yo\'nalishingizni tanlang:', reply_markup=markup)

# Handle section selection and send data to admins
@bot.message_handler(func=lambda message: True, content_types=['text'])
def section_choice(message):
    user_id = message.from_user.id
    # Check if all previous information has been collected
    if user_id in user_data and 'phone_number' in user_data[user_id] and 'region' in user_data[user_id] and 'district' in user_data[user_id]:
        chosen_section = message.text
        user_data[user_id]['chosen_section'] = chosen_section  # Store chosen section

        # Send confirmation to the user based on language preference
        if user_data[user_id]['language'] == 'en':
            bot.send_message(message.chat.id, "Thank you for providing your details! You will receive updates soon.")
        else:
            bot.send_message(message.chat.id, "Ma'lumotlaringiz uchun rahmat! Tez orada yangiliklarni olasiz.")

            # Prepare the message to send to admins
        admin_message = (
            f"🆕 New Registration:\n\n"
            f"📄 Name: {user_data[user_id]['name']}\n"
            f"🎂 Birth Date: {user_data[user_id]['birth_date']}\n"
            f"📞 Phone Number: {user_data[user_id]['phone_number']}\n"
            f"📍 Region: {user_data[user_id]['region']}\n"
            f"🌍 District: {user_data[user_id]['district']}\n"
            f"📝 Section: {user_data[user_id]['chosen_section']}"
        )

        # Send the admin message to both admins
        bot.send_message(ADMIN_ID1, admin_message)
        bot.send_message(ADMIN_ID2, admin_message)

bot.polling()



