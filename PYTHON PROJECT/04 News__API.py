## The NewsAPI and the requests module to fetch the daily news related to different topic..

import requests
API_KEY = "your_API"
Topic = input('Enter Your Topic: ')

url = "https://newsapi.org/v2/everything"

params = {
    "q": Topic,
    "sortBy": "publicshedAt",
    "language": "en",
    "apiKey": API_KEY
}

response = requests.get(url, params=params)
data = response.json()
print(data)
