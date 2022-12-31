import requests
from send_email import send_email
import json

topic = "nasa"

path = "configuration.json"
with open(path, "r") as handler:
    info = json.load(handler)

api_key = info["api"]
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2022-12-30&" \
      "language=en&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}"

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
