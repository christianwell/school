import requests # type: ignore # gører så jeg kan send ting til ntfy.sh
import feedparser # gører så jeg kan læse rss feeds

linkvejr = (
    "https://api.open-meteo.com/v1/forecast?"
    ""
    ","
    ""
    "&"
    "&"
    "&forecast_days=1"
    "&temporal_resolution=native"
    "&models=dmi_seamless"
)

response = requests.get(linkvejr)
data = response.json()

vejr = data["current_weather"]
nuvejr = vejr["temperature"]
d = feedparser.parse("https://www.dr.dk/nyheder/service/feeds/senestenyt")
entry = d["entries"][0]
nyhed1 = entry["title"]
linknyhed = entry["link"]
kanye = requests.get("https://api.kanye.rest/").json()["quote"]
ntfy = "https://ntfy.sh/"  # dit nfty topic

text = f'dagens sidste nyt er: ✏️ {nyhed1} ({linknyhed})\nKanye quote af i dag: "{kanye} " idags vejr er {nuvejr}°C. Husk at tage tøj på efter vejret! ☀️🌧️"'

requests.post(ntfy,data=text.encode('utf-8'),headers={"Title": "Godmorgen", "Priority": "high", "Tags": "morng"})

