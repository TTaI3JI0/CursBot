import logging
import requests
# Добавим необходимый объект из модуля telegram.ext
from telegram.ext import CommandHandler
from telegram.ext import Application
from telegram import ReplyKeyboardMarkup
from config import BOT_TOKEN, CURS_REQUEST
import schedule

# Выполняем запрос.
response = requests.get(CURS_REQUEST)
# Преобразуем ответ в json-объект
json_response = response.json()
valute_response = json_response['Valute']


def curs_update():
    global valute_response
    # Выполняем запрос.
    response = requests.get(CURS_REQUEST)
    # Преобразуем ответ в json-объект
    json_response = response.json()
    valute_response = json_response['Valute']


# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def values(update, context):
    reply_keyboard = [['/USD', '/EUR', '/KZT'],
                      ['/GBP', '/BYN', '/AED'],
                      ['/CNY', '/UAH', '/JPY'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text('Укажите валюту, курс которой вы хотите узнать', reply_markup=markup)


async def USD(update, context):
    reply_keyboard = [['/USD', '/EUR', '/KZT'],
                      ['/GBP', '/BYN', '/AED'],
                      ['/CNY', '/UAH', '/JPY'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(f'Один российский рубль равен '
                                    f'{float(valute_response["USD"]["Value"]) / float(valute_response["USD"]["Nominal"])} '
                                    f'{valute_response["USD"]["Name"]}',
                                    reply_markup=markup)


async def EUR(update, context):
    reply_keyboard = [['/USD', '/EUR', '/KZT'],
                      ['/GBP', '/BYN', '/AED'],
                      ['/CNY', '/UAH', '/JPY'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(f'Один российский рубль равен '
                                    f'{float(valute_response["EUR"]["Value"]) / float(valute_response["EUR"]["Nominal"])} '
                                    f'{valute_response["EUR"]["Name"]}',
                                    reply_markup=markup)


async def KZT(update, context):
    reply_keyboard = [['/USD', '/EUR', '/KZT'],
                      ['/GBP', '/BYN', '/AED'],
                      ['/CNY', '/UAH', '/JPY'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(f'Один российский рубль равен '
                                    f'{float(valute_response["KZT"]["Value"]) / float(valute_response["KZT"]["Nominal"])} '
                                    f'{valute_response["KZT"]["Name"]}',
                                    reply_markup=markup)


async def GBP(update, context):
    reply_keyboard = [['/USD', '/EUR', '/KZT'],
                      ['/GBP', '/BYN', '/AED'],
                      ['/CNY', '/UAH', '/JPY'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(f'Один российский рубль равен '
                                    f'{float(valute_response["GBP"]["Value"]) / float(valute_response["GBP"]["Nominal"])} '
                                    f'{valute_response["GBP"]["Name"]}',
                                    reply_markup=markup)


async def BYN(update, context):
    reply_keyboard = [['/USD', '/EUR', '/KZT'],
                      ['/GBP', '/BYN', '/AED'],
                      ['/CNY', '/UAH', '/JPY'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(f'Один российский рубль равен '
                                    f'{float(valute_response["BYN"]["Value"]) / float(valute_response["BYN"]["Nominal"])} '
                                    f'{valute_response["BYN"]["Name"]}',
                                    reply_markup=markup)


async def AED(update, context):
    reply_keyboard = [['/USD', '/EUR', '/KZT'],
                      ['/GBP', '/BYN', '/AED'],
                      ['/CNY', '/UAH', '/JPY'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(f'Один российский рубль равен '
                                    f'{float(valute_response["AED"]["Value"]) / float(valute_response["AED"]["Nominal"])} '
                                    f'{valute_response["AED"]["Name"]}',
                                    reply_markup=markup)


async def CNY(update, context):
    reply_keyboard = [['/USD', '/EUR', '/KZT'],
                      ['/GBP', '/BYN', '/AED'],
                      ['/CNY', '/UAH', '/JPY'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(f'Один российский рубль равен '
                                    f'{float(valute_response["CNY"]["Value"]) / float(valute_response["CNY"]["Nominal"])} '
                                    f'{valute_response["CNY"]["Name"]}',
                                    reply_markup=markup)


async def UAH(update, context):
    reply_keyboard = [['/USD', '/EUR', '/KZT'],
                      ['/GBP', '/BYN', '/AED'],
                      ['/CNY', '/UAH', '/JPY'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(f'Один российский рубль равен '
                                    f'{float(valute_response["UAH"]["Value"]) / float(valute_response["UAH"]["Nominal"])} '
                                    f'{valute_response["UAH"]["Name"]}',
                                    reply_markup=markup)


async def JPY(update, context):
    reply_keyboard = [['/USD', '/EUR', '/KZT'],
                      ['/GBP', '/BYN', '/AED'],
                      ['/CNY', '/UAH', '/JPY'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(f'Один российский рубль равен '
                                    f'{float(valute_response["JPY"]["Value"]) / float(valute_response["JPY"]["Nominal"])} '
                                    f'{valute_response["JPY"]["Name"]}',
                                    reply_markup=markup)


async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    user = update.effective_user
    reply_keyboard = [['/values'],
                      ['/help']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я бот, который знает курс всех валют по данным ЦБ. Хочешь что-то узнать?",
        reply_markup=markup)


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    reply_keyboard = [['/values'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text("USD - Доллар США\n"
                                    "EUR - Евро\n"
                                    "KZT - Казахстанских тенге\n"
                                    "GBP - Фунт стерлингов Соединенного королевства\n"
                                    "BYN - Белорусский рубль\n"
                                    "AED - Дирхам ОАЭ\n"
                                    "CNY - Китайский юань\n"
                                    "UAH - Украинских гривен\n"
                                    "JPY - Японских иен",
                                    reply_markup=markup)


def main():
    # Создаём объект Application.
    application = Application.builder().token(BOT_TOKEN).build()

    # Создаём обработчик сообщений типа filters.TEXT
    # из описанной выше асинхронной функции echo()
    # После регистрации обработчика в приложении
    # эта асинхронная функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.

    # Регистрируем обработчик в приложении.
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("back", start))
    application.add_handler(CommandHandler("values", values))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("USD", USD))
    application.add_handler(CommandHandler("EUR", EUR))
    application.add_handler(CommandHandler("KZT", KZT))
    application.add_handler(CommandHandler("GBP", GBP))
    application.add_handler(CommandHandler("BYN", BYN))
    application.add_handler(CommandHandler("AED", AED))
    application.add_handler(CommandHandler("CNY", CNY))
    application.add_handler(CommandHandler("UAH", UAH))
    application.add_handler(CommandHandler("JPY", JPY))

    # Запускаем приложение.
    application.run_polling()


schedule.every().day.at("00:00").do(curs_update)
# каждый день в 00:00 обновление

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
