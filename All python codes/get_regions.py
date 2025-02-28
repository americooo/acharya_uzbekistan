from telebot import types, TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from get_district import *

# Define districts for each region
districts_by_region = {
    "Termiz": ["Angor tumani", "Bandixon tumani", "Boysun tumani", "Denov tumani", "Jarqo`rg`on tumani", "Muzrabot tumani", "Oltinsoy tumani", "Qiziriq tumani", "Qumqo`rg`on tumani", "Sariosiyo tumani", "Sherobot tumani", "Sho`rchi tumani", "Uzun tumani"],
    "Surxondaryo": ["Angor tumani", "Bandixon tumani", "Boysun tumani", "Denov tumani", "Jarqo`rg`on tumani", "Muzrabot tumani", "Oltinsoy tumani", "Qiziriq tumani", "Qumqo`rg`on tumani", "Sariosiyo tumani", "Sherobot tumani", "Sho`rchi tumani", "Uzun tumani"],
    "Farg`ona": ["Beshariq tumani", "Bog`dod tumani", "Buvayda tumani", "Dang`ara tumani", "Farg`ona shahri", "Farg`ona tumani", "Furqat tumani", "Marg`ilon shahri", "O`zbekiston tumani", "Oltiariq tumani", "Qo`qon shahri", "Qo`shtepa tumani", "Quva tumani", "Quvasoy shahri", "Rishton tumani", "So`x tumani", "Toshloq tumani", "Uchko`prik tumani", "Yozyovon tumani"],
    "Navoiy": ["Konimex tumani", "Navbahor tumani", "Navoiy tumani", "Nurota tumani", "Qiziltepa tumani", "Tomdi tumani", "Uchquduq tumani", "Xatirchi tumani"],
    "Bukhara": ["Buxoro shahar", "G`ijduvon tumani", "Jondor tumani", "Kogon tumani", "Olot tumani", "Peshku tumani", "Qorako`l tumani", "Qorovulbozor tumani", "Romitan tumani", "Shofirkon tumani", "Vobkent tumani"],
    "Qashqadaryo": ["Chiroqchi tumani", "Dehqonobod tumani", "Gʻuzor tumani", "Kasbi tumani", "Kitob tumani", "Koson tumani", "Mirishkor tumani", "Muborak tumani", "Nishon tumani", "Qamashi tumani", "Qarshi tumani", "Shahrisabz tumani", "Yakkabog` tumani"],
    "Xorazm": ["Bog`ot tumani", "Gurlan tumani", "Hazorasp tumani", "Qo`shko`pir tumani", "Shovot tumani", "Urganch tumani", "Xiva tumani", "Xonqa tumani", "Yangiariq tumani", "Yangibozor tumani"],
    "Jizzax": ["Arnasoy tumani", "Baxmal tumani", "Do`stlik tumani", "Forish tumani", "G`allaorol tumani", "Jizzax tumani", "Mirzacho`l tumani", "Paxtakor tumani", "Sharof Rashidov tumani", "Yangiobod tumani", "Zafarobod tumani", "Zarbdor tumani", "Zomin tumani"],
    "Nukus": ["Amudaryo tumani", "Beruniy tumani", "Chimboy tumani", "Ellikqala tumani", "Kegeyli tumani", "Mo`ynoq tumani", "Nukus shahri", "Nukus tumani", "Qonliko`l tumani", "Qorauzaq tumani", "Qung`irot tumani", "Shumanay tumani", "Taxiatosh shahri", "Taxtako`pir tumani", "To`rtko`l tumani", "Xo`jayli tumani"],
    "Samarqand": ["Bulung`ur tumani", "Ishtixon tumani", "Jomboy tumani", "Kattaqo`rg`on shahri", "Kattaqo`rg`on tumani", "Narpay tumani", "Nurobod tumani", "Oqdaryo tumani", "Past darg`om tumani", "Paxtachi tumani", "Poyariq tumani", "Qo`shrabot tumani", "Samarqand shahri", "Samarqand tumani", "Toyloq tumani", "Urgut tumani"],
    "Sirdaryo": ["Boyovut tumani", "Guliston tumani", "Mirzaobod tumani", "Oqoltin tumani", "Sayxunobod tumani", "Sardoba tumani", "Sirdaryo tumani", "Xovos tumani"],
    "Toshkent shahar": ["Bektemir tumani", "Chilonzor tumani", "Mirobod tumani", "Mirzo Ulug`bek tumani", "Olmazor tumani", "Sergeli tumani", "Shayhontohur tumani", "Uchtepa tumani", "Yakkasaroy tumani", "Yashnaobod tumani", "Yunusobod tumani"]
}



def generate_region_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    # Assuming you have a list of regions to display
    regions = ['Termiz','Surxondaryo','Farg`ona','Navoiy','Bukhara','Qashqadaryo','Xorazm','Jizzax','Nukus','Samarqand','Sirdaryo','Toshkent shahar']

    for region in regions:
        button = types.InlineKeyboardButton(text=region, callback_data=f'region_{region}')
        keyboard.add(button)

    return keyboard

def register_get_region_handler(bot: TeleBot, user_data: dict, generate_district_keyboard):
    @bot.callback_query_handler(func=lambda call: call.data.startswith("region_"))
    def get_region(call):
        region = call.data.split("_")[1]  # Extract selected region
        user_id = call.from_user.id
        user_data[user_id]['region'] = region  # Store region

        # Send district selection message
        bot.send_message(
            call.message.chat.id,
            "Please select your district:" if user_data[user_id].get('language', 'en') == 'en' else "Iltimos, tumanni tanlang:",
            reply_markup=generate_district_keyboard(region)
        )



def generate_district_keyboard(region):
    # Example regions and districts mapping
    districts = districts_by_region

    keyboard = InlineKeyboardMarkup()  # Correct keyboard type
    for district in districts.get(region, []):
        # Add buttons to the keyboard
        keyboard.add(InlineKeyboardButton(district, callback_data=f"district_{district}"))

    return keyboard

# def register_get_region_handler(bot, user_data, generate_district_keyboard):


