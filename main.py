import requests
from send_email import send_email

api_key = "cee1fae7354e487cb51bd4bb69f3dd42"
url = "https://newsapi.org/v2/everything?q=nasa&" \
      "from=2022-11-30&language=en&sortBy=publishedAt&apiKey=" \
      "cee1fae7354e487cb51bd4bb69f3dd42"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
