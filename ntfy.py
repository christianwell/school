import requests# gører så jeg kan send ting til ntfy.sh
import feedparser# gører så jeg kan læse rss feeds
import time
from datetime import datetime

d = feedparser.parse("https://www.dr.dk/nyheder/service/feeds/senestenyt")
entry = d["entries"][0]
nyhed1 = entry["title"]
linknyhed = entry["link"]
kanye = requests.get("https://api.kanye.rest/").json()["quote"]
tid = "07:00"
ntfy = "https://ntfy.sh/your_topic"  # dit nfty topic
text = f'Godmorgen, dagens sidste nyt er: ✏️ {nyhed1} ({linknyhed})\nKanye quote af i dag: "{kanye}"'

while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == tid:
        requests.post("", data=text.encode('utf-8'))
        break
    time.sleep(30)

    
