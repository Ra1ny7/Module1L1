import telebot
from config import TOKEN
from logic import gen_pass
from logic import flip_coin    
# Инициализация бота с использованием его токена
bot = telebot.TeleBot(TOKEN)

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
@bot.message_handler(content_types=['photo'])
def send_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    download_file = bot.download_file(file_info.file_path)
    file_path = 'img/' + f'{message.photo[-1].file_id}.jpg'
    with open(file_path, 'wb') as file:
        file.write(download_file)
    bot.reply_to(message, "Скачал твою отправленную картинку")
# Handle '/start' and '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am TeraBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['password'])
def generate_password(message):
    len_pass=telebot.util.extract_arguments(message.text)
    bot.send_message(message.chat.id, str(gen_pass(int(len_pass))))

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
# Запуск бота
bot.polling()