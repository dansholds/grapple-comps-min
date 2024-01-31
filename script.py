import requests
from bs4 import BeautifulSoup

url = "https://smoothcomp.com/en/events/upcoming"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

event_cards = soup.find_all("div", class_="event-title margin-bottom-xs-8")
hrefs = [card.a["href"] for card in event_cards]

print(hrefs)