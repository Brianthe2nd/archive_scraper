from bs4 import BeautifulSoup
from pprint import pprint
import requests
import json
def get_data():

    url = "https://web.archive.org/web/20200618041758/https://twitter.com/NekroVEVO/status/1273468328594423808"

    payload = {}
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'eu_cn=1; _ga=GA1.2.1222850462.1592453982; _gid=GA1.2.2068325462.1592453982; donation-identifier=eec8674e00c06dc27c56db16cb5479f1; donation=x',
    'priority': 'u=0, i',
    'referer': 'https://web.archive.org/web/*/twitter.com/NekroVevo*',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    return response.text

res=get_data()
soup = BeautifulSoup(res,features="html.parser")
author = soup.select_one("div.ReplyingToContextBelowAuthor  span.username").text.strip()
# print(author)
reply_time =soup.select_one("div.js-tweet-details-fixer  span.metadata > span").text.strip()
# print(reply_time)
likes =soup.select_one("li.js-stat-count strong").text.strip()
# print(likes)
reply =soup.select_one("p.js-tweet-text").text.strip()
# print(reply)

json_data ={"Author":author,
            "Reply":reply,
            "Reply_time":reply_time,
            "Likes":likes}

pprint(json_data)
with open("data.json", "w") as file:
    json.dump(json_data, file , indent =4)
