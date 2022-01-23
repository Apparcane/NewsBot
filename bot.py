from tokens import *
import telebot
from telebot import types
import json

bot = telebot.TeleBot(BOT_API)  # @appdouvenderbot

@bot.message_handler(commands=['start', 'go'])
def start(message):
    print("Id: " + str(message.from_user.id) + "\nFirst Name: " +
          str(message.from_user.first_name) + "\nText: " + str(message.text) + "\n")
    bot.send_message(message.chat.id, "Воспользуйся командой - /news")

@bot.message_handler(commands=['news'])
def news(message):
    print("Id: " + str(message.from_user.id) + "\nFirst Name: " +
          str(message.from_user.first_name) + "\nText: " + str(message.text) + "\n")
    
    with open('./json/news.json') as news_file:
        data = json.load(news_file)
    articles = data['articles']
    
    if data['totalResults'] == 0:
        bot.send_message(message.chat.id, "Свежих новостей нет.")
        
    else:
        for articl in articles:
            if articl['author'] == None:
                articl['author'] = 'Не указан'
                
            bot.send_message(
                            message.chat.id, 
                            "Свежие новости: " +  '\n' +
                            'Источник: ' + articl['source']['name'] + '\n' +
                            'Автор: ' + articl['author'] +  '\n\n' +
                            articl['title'] + '\n' +
                            articl['description'] +  '\n\n' +
                            'Ссылка: ' + articl['url']                        
                            )

bot.polling(none_stop=True)