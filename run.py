# -*- coding: utf-8 -
import telebot
from bs4 import BeautifulSoup
import requests
from random import randint
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



TOKEN = '1085423235:AAE2VP0HgEaEe4yH1ecLGExD5CQQv8D1zaI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi I am your bot assistant😁, enter the command /help to see a list of commands that you can write to me')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, ' /weather - Weather in Belarus \n /news - News in world \n /films - Films in cinema today')
    
@bot.message_handler(commands=['weather'])
def weather(message):
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    resp = requests.get("https://www.gismeteo.by/weather-orsha-4236/", headers = headers).text
    soup = BeautifulSoup(resp, "html.parser")
    
    #find
    title = soup.find("span", class_ = "tab-weather__value_l")
    weath = title.get_text()
    bot.send_message(message.chat.id, 'Now in Belarus:')
    time.sleep(0.3)
    bot.send_message(message.chat.id, weath)

@bot.message_handler(commands=['news'])
def news(message):

    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    resp = requests.get("https://www.bbc.com/news/world", headers = headers).text
    soup = BeautifulSoup(resp, "html.parser")
    
    #find
    title = soup.findAll("h3", class_ = "gs-c-promo-heading__title")
    bot.send_message(message.chat.id, 'Last news:')
    for i in range(1,6):
        bot.send_message(message.chat.id, title[i].text)
    
@bot.message_handler(commands=['films'])
def films(message):
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    resp = requests.get("https://afisha.relax.by/kino/minsk/", headers = headers).text
    soup = BeautifulSoup(resp, "html.parser")
    
    #find
    title = soup.findAll("span", class_ = "afishaSlider__text")
    bot.send_message(message.chat.id, 'Films in cinema (in russian)')
    for i in range(0,len(title)):
        bot.send_message(message.chat.id, title[i].text)
        if i > 10:
            break

# text
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello, hello😊')
    else:
        bot.send_message(message.chat.id, 'I don’t understand you, write a command /help to get a list of commands')

    

bot.polling(none_stop=True)