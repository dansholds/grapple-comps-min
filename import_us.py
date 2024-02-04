from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage
driver.get('https://smoothcomp.com/en/events/upcoming')

# Wait for the input element to be visible
wait = WebDriverWait(driver, 10)
input_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.multiselect-tags-search")))

# Values to enter
values = [
    "Jiu-Jitsu (Gi)",
    "Jiu-Jitsu (NoGi)",
    "Jiu-Jitsu (NoGi) - ADCC",
    "Jiu-Jitsu (NoGi) - Submission Wrestling"
]

# Enter each value
for value in values:
    input_element.click()  # Focus the input element
    input_element.clear()  # Clear the input element
    input_element.send_keys(value)  # Type the value
    input_element.send_keys(Keys.ENTER)  # Simulate pressing Enter to select the value

# Initialize a list to hold URLs
uk_event_urls = []

# Find all event cards
event_cards = driver.find_elements(By.CSS_SELECTOR, '.event-card')

for card in event_cards:
    # Check if the event card's location contains "United States"
    location = card.find_element(By.CSS_SELECTOR, '.location.truncate').text
    if "United States" in location:
        # If so, extract the URL from the anchor tag within the event card
        event_url = card.find_element(By.CSS_SELECTOR, 'a.image-container').get_attribute('href')
        uk_event_urls.append(event_url)

# Close the browser
driver.quit()

# Write the UK event URLs to a file
with open('us_events.txt', 'w') as file:
    for url in uk_event_urls:
        file.write(url + '\n')
