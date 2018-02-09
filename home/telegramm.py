import telepot

token = '389460165:AAEimDJ0HY3tJk9sd9HX1iHvjjUIG0hhAtM'
my_id = 177914540
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(177914540, text, parse_mode="Markdown")