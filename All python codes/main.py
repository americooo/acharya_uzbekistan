# # import telebot
# # from telebot import types
# #
#
#
# import telebot
# from telebot import types
#
# # API_TOKEN = '6445543196:AAHG9mjlmC9AbhO8xStWz6Pws6Yg0k75WI4'
# # ADMIN_ID1 = '1861209145'
# # ADMIN_ID2 = '5313781530'  # Ensure this is the correct admin ID
#
#districts_by_region = {
#     "Termiz": ["Angor tumani", "Bandixon tumani", "Boysun tumani", "Denov tumani", "Jarqo`rg`on tumani","Muzrabot tumani", "Oltinsoy tumani", "Qiziriq tumani", "Qumqo`rg`on tumani", "Sariosiyo tumani", "Sherobot tumani", "Sho`rchi tumani", "Uzun tumani"],
#     "Surxondaryo": ["Angor tumani", "Bandixon tumani", "Boysun tumani","Denov tumani","Jarqo`rg`on tumani","Muzrabot tumani","Oltinsoy tumani","Qiziriq tumani","Qumqo`rg`on tumani","Sariosiyo tumani","Sherobot tumani","Sho`rchi tumani","Uzun tumani"],
#     "Farg`ona": ["Beshariq tumani","Bog`dod tumani","Buvayda tumani	","Dang`ara tumani","Farg`ona shahri","Farg`ona tumani","Furqat tumani","Marg`ilon shahri","O`zbekiston tumani","Oltiariq tumani","Qo`qon shahri","Qo`shtepa tumani","Quva tumani","Quvasoy shahri","Rishton tumani","So`x tumani","Toshloq tumani","Uchko`prik tumani","Yozyovon tumani"],
#     "Navoiy": ["Konimex tumani","Navbahor tumani","Navoiy tumani","Nurota tumani","Qiziltepa tumani","Tomdi tumani","Uchquduq tumani","Xatirchi tumani"],
#     "Bukhara": ["Buxoro tumani","G`ijduvon tumani ","Jondor tumani","Kogon tumani ","Olot tumani","Peshku tumani","Qorako`l tumani","Qorovulbozor tumani","Romitan tumani","Shofirkon tumani","Vobkent tumani"],
#     "Qashqadaryo": ["Chiroqchi tumani","Dehqonobod tumani","Gʻuzor tumani ","Kasbi tumani ","Kitob tumani","Koson tumani","Mirishkor tumani","Muborak tumani","Nishon tumani","Qamashi tumani","Qarshi tumani","Shahrisabz tumani","Yakkabog` tumani"],
#     "Xorazm": ["Bog`ot tumani","Gurlan tumani","Hazorasp tumani","Qo`shko`pir tumani","Shovot tumani","Urganch tumani","Xiva tumani","Xonqa tumani ","Yangiariq tumani","Yangibozor tumani"],
#     "Jizzax": ["Arnasoy tumani","Baxmal tumani","Do`stlik tumani","Forish tumani ","G`allaorol tumani "," Jizzax tumani","Mirzacho`l tumani ","Paxtakor tumani ","Sharof Rashidov tumani ","Yangiobod tumani","Zafarobod tumani","Zarbdor tumani","Zomin tumani"],
#     "Nukus": ["Amudaryo tumani","Beruniy tumani","Chimboy tumani","Ellikqala tumani","Kegeyli tumani","Mo`ynoq tumani","Nukus shahri","Nukus tumani","Qonliko`l tumani","Qorauzaq tumani","Qung`irot tumani","Shumanay tumani","Taxiatosh shahri","Taxtako`pir tumani","To`rtko`l tumani","Xo`jayli tumani"],
#     "Samarqand": ["	Bulung`ur tumani","Ishtixon tumani","Jomboy tumani","Kattaqo`rg`on shahri","Kattaqo`rg`on tumani","Narpay tumani","Nurobod tumani","Oqdaryo tumani","Past darg`om tumani","Paxtachi tumani","Poyariq tumani","Qo`shrabot tumani","Samarqand shahri","Samarqand tumani","Toyloq tumani","Urgut tumani"],
#     "Sirdaryo": ["Boyovut tumani","Guliston tumani","Mirzaobod tumani","Oqoltin tumani","Sayxunobod tumani","Sardoba tumani","Sirdaryo tumani","Xovos tumani"],
#     "Toshkent shahar": ["Bektemir tumani","Chilonzor tumani","Mirobod tumani","Mirzo Ulug`bek tumani","Olmazor tumani","Sergeli tumani","Shayhontohur tumani","Uchtepa tumani","Yakkasaroy tumani","Yashnaobod tumani","Yunusobod tumani"],
#     #   # Add other regions and districts...
# }

import telebot
from start_handlers import start, handle_language_selection
from user_details_handlers import get_name, get_birth_date, handle_phone_number
from admin_handlers import admin_command
from get_regions import *
# from get_regions import register_get_region_handler
# from sections import get_sections_keyboard
# from get_district import generate_district_keyboard  # Import the function

# Now, pass all three required arguments
# register_get_region_handler(bot, user_data, generate_district_keyboard)


API_TOKEN = '6445543196:AAHG9mjlmC9AbhO8xStWz6Pws6Yg0k75WI4'
bot = telebot.TeleBot(API_TOKEN)

ADMIN_ID1 = '1861209145'
# ADMIN_ID2 = '5313781530'

CHANNEL_ID = '-1002250391416'


user_data = {}  # Dictionary to store user data



# Command to start the bot
@bot.message_handler(commands=['start'])
def start_command(message):
    start(bot, message)

# Callback handler for language selection
@bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
def language_selection(call):
    handle_language_selection(bot, call, user_data)

# Command for admin functionality
@bot.message_handler(commands=['admin'])
def admin(message):
    admin_command(bot, message)

# Message handler for collecting the user's name
@bot.message_handler(func=lambda message: message.from_user.id not in user_data or 'name' not in user_data[message.from_user.id])
def name_handler(message):
    get_name(bot, message, user_data)

# Message handler for collecting the user's birth date
@bot.message_handler(func=lambda message: message.from_user.id in user_data and 'birth_date' not in user_data[message.from_user.id])
def birth_date_handler(message):
    get_birth_date(bot, message, user_data)

# Message handler for collecting the user's phone number
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
        bot.send_message(CHANNEL_ID, admin_message)

bot.polling()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------









#