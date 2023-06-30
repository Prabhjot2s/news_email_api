import requests
from emails import to_send
import time

today = time.strftime("%Y-%M-%d")
print(today)

api_key = '216c00cdfd694e7c8377913f1d6557a7'
url = 'https://newsapi.org/v2/' 'everything?' \
      'q=canada&' \
      'language=en&' \
      'sortBy=popularity&' \
      'apiKey=216c00cdfd694e7c8377913f1d6557a7'

values = requests.get(url)
title = []
description = []
content = values.json()
message = ''

for articles in content['articles'][0:20]:
    message = message + (articles['title']) + '\n'
    message = message + (articles['description']) + '\n'
    message = message + (articles['url']) + '\n' + '\n'

message = f"""\
Subject: Your News update for Today 

{message}"""

message = message.encode('utf-8')

to_send(message)
