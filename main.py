import requests
from send_email import send_email

topic = "nasa"

api_key = "cee1fae7354e487cb51bd4bb69f3dd42"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2022-12-30&" \
      "language=en&" \
      "sortBy=publishedAt&" \
      "apiKey=cee1fae7354e487cb51bd4bb69f3dd42"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Todays news"\
               + "\n" + body + article["title"]\
               + "\n" + article["description"]\
               + "\n" + article["url"] + 2* "\n"

body = body.encode("utf-8")
send_email(message=body)
