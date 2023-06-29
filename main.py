import requests

api_key='216c00cdfd694e7c8377913f1d6557a7'
url='https://newsapi.org/v2/' \
    'everything?q=tesla&from=2023-05-29&sortBy=publishedAt&' \
    'apiKey=216c00cdfd694e7c8377913f1d6557a7'
values=requests.get(url)

content=values.json()

for articles in content['articles']:
    print(articles['title'])