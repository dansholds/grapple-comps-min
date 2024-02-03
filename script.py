from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage
driver.get('https://smoothcomp.com/en/events/upcoming')

# Wait for the dynamic content to load
driver.implicitly_wait(10)  # This waits up to 10 seconds before throwing a NoSuchElementException

# Initialize a list to hold URLs
uk_event_urls = []

# Find all event cards
event_cards = driver.find_elements(By.CSS_SELECTOR, '.event-card')

for card in event_cards:
    # Check if the event card's location contains "United Kingdom"
    location = card.find_element(By.CSS_SELECTOR, '.location.truncate').text
    if "United Kingdom" in location:
        # If so, extract the URL from the anchor tag within the event card
        event_url = card.find_element(By.CSS_SELECTOR, 'a.image-container').get_attribute('href')
        uk_event_urls.append(event_url)

# Close the browser
driver.quit()

# Write the UK event URLs to a file
with open('uk_events.txt', 'w') as file:
    for url in uk_event_urls:
        file.write(url + '\n')
