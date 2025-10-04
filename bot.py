import telebot
from model_loader import predict_image
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

TEMP_DIR = "temp_images"
os.makedirs(TEMP_DIR, exist_ok=True)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Отправь фото кота или собаки, а я скажу, кто на картинке 🐱🐶")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_message(message.chat.id, "Получил фото, распознаю...")

    # Берем фото самого высокого качества
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    temp_path = os.path.join(TEMP_DIR, f"{message.photo[-1].file_id}.jpg")
    with open(temp_path, 'wb') as f:
        f.write(downloaded_file)

    # Делаем предсказание через модель
    result = predict_image(temp_path)
    bot.send_message(message.chat.id, f"Это: {result}")

    # Удаляем временный файл
    os.remove(temp_path)

bot.polling(none_stop=True)
