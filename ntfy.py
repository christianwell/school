import requests # gører så jeg kan send ting til ntfy.sh
import feedparser # gører så jeg kan læse rss feeds
import time
d = feedparser.parse("https://www.dr.dk/nyheder/service/feeds/senestenyt")
entry=d["entries"][1]
nyhed1 = entry["title"] 
linknyhed = entry["link"]
kanye = requests.get("https://api.kanye.rest/").json()["quote"]


text = f'Godmorgen , dagens sidste nyt er: ✏️ {linknyhed}{nyhed1} : Kanye quote af i dag: {kanye}'


requests.post("https://ntfy.sh/", 
    text.encode(encoding='utf-8'))
