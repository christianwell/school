import requests # gører så jeg kan send ting til ntfy.sh
import feedparser # gører så jeg kan læse rss feeds
import time
linkvejr = "https://api.open-meteo.com/v1/forecast?latitude=55.1964&longitude=10.251&daily=weather_code,temperature_2m_max,apparent_temperature_max,temperature_2m_min,apparent_temperature_min,daylight_duration,sunset,sunrise&current_weather=true&timezone=auto&forecast_days=1&temporal_resolution=native&models=dmi_seamless"
response = requests.get(linkvejr)
data = response.json()  
nuvejr = data["current_weather"]
nuvejr = nuvejr["temperature"]
d = feedparser.parse("https://www.dr.dk/nyheder/service/feeds/senestenyt")
entry = d["entries"][0]
nyhed1 = entry["title"]
linknyhed = entry["link"]
kanye = requests.get("https://api.kanye.rest/").json()["quote"]
ntfy = "https://ntfy.sh/"  # dit nfty topic

text = f'dagens sidste nyt er: ✏️ {nyhed1} ({linknyhed})\nKanye quote af i dag: "{kanye} " idags vejr er {nuvejr}°C. Husk at tage tøj på efter vejret! ☀️🌧️"'

requests.post(ntfy,data=text.encode('utf-8'),headers={"Title": "Godmorgen", "Priority": "high", "Tags": "morng"})
