import requests
from bs4 import BeautifulSoup

url = "https://smoothcomp.com/en/event/13781"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object with the response content
soup = BeautifulSoup(response.content, "html.parser")

# Extract the first h1 element
h1_element = soup.find("h1")
h1_text = h1_element.text.strip()

# Extract the text below the "Event Starts" title
info_element = soup.find("h2", text="Event Starts").find_next(class_="info")
info_text = info_element.text.strip()

# Extract all text within the "information margin-bottom-xs-64" class
info_margin_elements = soup.find_all(class_="information margin-bottom-xs-64")
info_margin_text = [element.text.strip() for element in info_margin_elements]

print("First h1 element:", h1_text)
print("Text below 'Event Starts':", info_text)
print("Text within 'information margin-bottom-xs-64' class:")
for text in info_margin_text:
    print(text)