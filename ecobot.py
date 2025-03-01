import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot(TOKEN)


import random

eco_tips = [
    "Используй многоразовые сумки вместо пластиковых пакетов.",
    "Выключай свет, выходя из комнаты — это экономит энергию.",
    "Сократи потребление одноразового пластика — возьми с собой свою бутылку с водой.",
    "Компостируй органические отходы — это уменьшает количество мусора на свалках.",
    "Сажай деревья — они очищают воздух и создают тень."
]

@bot.message_handler(commands=['advice'])
def give_advice(message):
    tip = random.choice(eco_tips)
    bot.send_message(message.chat.id, f"🌿 Совет: {tip}")

items={
    "btn1": ("📜 Бумага", "2-10 недель"),
    "btn2": ("🍌 Банановая кожура", "2-5 недель"),
    "btn3": ("📰 Газета", "6 недель"),
    "btn4": ("👕 Хлопчатобумажная ткань", "2-5 месяцев"),
    "btn5": ("🧶 Шерстяная ткань", "1-5 лет"),
    "btn6": ("🥫 Консервная банка", "50 лет"),
    "btn7": ("🛍️ Пластиковый пакет", "100-500 лет"),
    "btn8": ("🥤 Алюминиевая банка", "200-500 лет"),
    "btn9": ("🍾 Стеклянная бутылка", "более 1000 лет"),
    "btn10": ("🥤 Пластиковая бутылка", "450 лет"),
    "btn11": ("♻️ Пенопласт", "более 500 лет"),
    "btn12": ("🪵 Деревянная доска", "10-15 лет"),
    "btn13": ("🍬 Жевательная резинка", "более 100 лет"),
    "btn14": ("🚬 Окурок сигареты", "1-5 лет"),
    "btn15": ("🛞 Резиновая покрышка", "50-80 лет"),
    }
def get_inline_keyboard():
  markup=InlineKeyboardMarkup()
  markup.add(InlineKeyboardButton('📜 Бумага', callback_data='btn1'))
  markup.add(InlineKeyboardButton('🍌 Банановая кожура', callback_data='btn2'))
  markup.add(InlineKeyboardButton('📰 Газета', callback_data='btn3'))
  markup.add(InlineKeyboardButton('👕 Хлопчатобумажная ткань', callback_data='btn4'))
  markup.add(InlineKeyboardButton('🧶 Шерстяная ткань', callback_data='btn5'))
  markup.add(InlineKeyboardButton('🥫 Консервная банка', callback_data='btn6'))
  markup.add(InlineKeyboardButton('🛍️ Пластиковый пакет', callback_data='btn7'))
  markup.add(InlineKeyboardButton('🥤 Алюминиевая банка', callback_data='btn8'))
  markup.add(InlineKeyboardButton('🍾 Стеклянная бутылка', callback_data='btn9'))
  markup.add(InlineKeyboardButton('🥤 Пластиковая бутылка', callback_data='btn10'))
  markup.add(InlineKeyboardButton('♻️ Пенопласт', callback_data='btn11'))
  markup.add(InlineKeyboardButton('🪵 Деревянная доска', callback_data='btn12'))
  markup.add(InlineKeyboardButton('🍬 Жевательная резинка', callback_data='btn13'))
  markup.add(InlineKeyboardButton('🚬 Окурок сигареты', callback_data='btn14'))
  markup.add(InlineKeyboardButton('🛞 Резиновая покрышка', callback_data='btn15'))
  return markup
@bot.message_handler(commands=['start','help'])
def starting(message):
  bot.send_message(message.chat.id, 'Привет! Я эко-бот. Напиши мне команду /eco')
@bot.message_handler(commands=['eco'])
def eco_items(message):
  bot.send_message(message.chat.id, 'Выбери предмет, для которого хочешь узнать сколько он разлагается', reply_markup=get_inline_keyboard())
@bot.callback_query_handler(func=lambda call: call.data in items)
def callback_handler(call):
    name, decay_time = items[call.data]
    bot.send_message(call.message.chat.id, f"{name} разлагается за {decay_time}.")
bot.infinity_polling()
