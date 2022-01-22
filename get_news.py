from time import sleep
from classes import *
from token import *
from newsapi import NewsApiClient
from tokens import News_tokken
import json

# mail = message

i = 0

while True:
    newsapi = NewsApiClient(api_key=News_tokken)
    data = newsapi.get_top_headlines(language='ru', country='ua')
    data = json.dumps(data)
    data = json.loads(str(data))
    articles = data['articles']

    with open('./json/news.json', 'w', encoding = 'utf-8') as outfile:
        json.dump(data, outfile, indent = 4)
    
    print("Цыкл: " + str(i))
    i += 1
    sleep(10000)


# for articl in articles:
#     mail = message(
#                source = articl['source']['name'], 
#                title = articl['title'], 
#                author = articl['author'], 
#                descript = articl['description'], 
#                url = articl['url']
#                )

# print(mail.display())