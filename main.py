import pyowm
import telebot
bot = telebot.TeleBot("6257599373:AAESCTq6VGO1Km6L3t_CBulkshBMUfK5R3k")
owm = pyowm.OWM('3baeddc0bdfaffea1ccae4e351d939e2')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который показывает погоду в городах. Для получения информации о погоде отправь мне название города.")
dictionary = {
    'clear sky': 'Ясно ☀',
    'few clouds': 'Малооблачно ⛅',
    'scattered clouds': 'Рассеянные облака ☁',
    'broken clouds': 'Облачно с прояснениями ⛅',
    'overcast clouds': 'Пасмурно 🌧',
    'mist': 'Туман 🌫',
    'haze': 'Мгла 🌫',
    'fog': 'Туман 🌫',
    'light rain': 'Небольшой дождь 💧',
    'moderate rain': 'Умеренно сильный дождь ☔',
    'heavy intensity rain': 'Сильный дождь 🌧',
    'very heavy rain': 'Очень сильный дождь 🌧🌨',
    'extreme rain': 'Экстремальный дождь 🌨🌨',
    'light snow': 'Небольшой снег 🌨',
    'moderate snow': 'Умеренно сильный снег 🌨',
    'heavy snow': 'Сильный снег 🌨🌨',
    'sleet': 'Мокрый снег 🌨💧',
    'light shower sleet': 'Небольшой мокрый снег 🌨💧',
    'shower sleet': 'Мокрый снег 🌨💧',
    'light rain and snow': 'Небольшой дождь со снегом🌧🌨',
    'rain and snow': 'Дождь со снегом 💧❄',
    'light shower snow': 'Небольшой снегопад 🌨❄',
    'shower snow': 'Снегопад🌨❄',
    'thunderstorm with light rain': 'Гроза, небольшой дождь ⚡💧',
    'thunderstorm with rain': 'Гроза, дождь ⚡☔',
    'thunderstorm with heavy rain': 'Гроза, сильный дождь ⚡⛈',
    'light thunderstorm': 'Небольшая гроза ⚡⛈',
    'thunderstorm': 'Гроза 🌩',
    'heavy thunderstorm': 'Сильная гроза 🌩',
    'ragged thunderstorm': 'Разрозненная гроза 🌩⚡',
    'thunderstorm with light drizzle': 'Гроза, небольшой моросящий дождь ⚡☔',
    'thunderstorm with drizzle': 'Гроза, моросящий дождь 🌩💧',
    'thunderstorm with heavy drizzle': 'Гроза, сильный моросящий дождь 🌩🌧',
    'freezing rain': 'Ледяной дождь 🧊🌧',
    'shower rain': 'Ливень 🌧',
    'heavy intensity shower rain': 'Сильный ливень 💧🌧',
    'ragged shower rain' : 'Разрозненный ливень 🌧🌧',
    'light intensity shower rain': 'небольшой дождь 💧',
    'unknown': 'Неизвестно'
}
@bot.message_handler(func=lambda message: True)
def send_weather(message):
    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temperature = w.get_temperature('celsius')['temp']
        status = w.get_detailed_status()
        if status in dictionary:
            status = dictionary[status]
        wind = w.get_wind()['speed']
        humidity = w.get_humidity()
        location = observation.get_location().get_name()
        country = observation.get_location().get_country()
        temperature = str(int(temperature))
        if country == 'UA':
            country = ''
        if country == 'RU':
            country = '🇷🇺'
        if int(temperature) >= 25:
            temperature = temperature + '°C' + ' 🔥'
        elif int(temperature) < -5:
            temperature = temperature + '°C'+ ' ⛄'
        else:
            temperature += '°C'
        response = f"Сейчас в {location} {country} ⬇\n{status}\nТемпература {temperature}\nСкорость ветра {int(wind)} м/с 🌬\nВлажность {humidity}% 💦"
    except pyowm.exceptions.api_response_error.NotFoundError:
        response = "Я не могу найти такой город. Пожалуйста, убедитесь, что вы правильно написали название города."
    bot.reply_to(message, response)
bot.polling()
