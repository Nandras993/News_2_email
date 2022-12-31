import requests

api_key = "cee1fae7354e487cb51bd4bb69f3dd42"
url = "https://newsapi.org/v2/everything?q=nasa&" \
      "from=2022-11-30&language=en&sortBy=publishedAt&apiKey=" \
      "cee1fae7354e487cb51bd4bb69f3dd42"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
