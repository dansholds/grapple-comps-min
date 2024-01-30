import sys
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from dateutil import parser

def extract_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        #Get Location & Cost
        list_item_texts = soup.find_all(class_="sc-list-item-text")
        location = [item.text.strip() for item in list_item_texts]

        #Extract Location
        place = [item.split('\n\n', 1)[1].split()[0] for item in location if '\n\n' in item]
        place = place[0]

        # Get highest price
        text = " ".join(location)
        numbers = re.findall(r"(\d+)\s+GBP", text)
        numbers = [int(num) for num in numbers]

        # Check if the list is not empty before calculating the maximum
        if numbers:
            price = max(numbers)
            price = "£" + str(price)
        else:
            print(f"No price found for {url}. Skipping...")
            return None

        # Get Title
        title_element = soup.find('h2', class_='margin-xs-0 flex-grow-1')
        title = title_element.get_text(strip=True) if title_element else "Placeholder Title"
        
        #Get Date
        date_element = soup.find('strong', class_='info')
        date = date_element.get_text() if date_element else "Placeholder Date"
        month = date.split(' ')[1].strip()

        #Format Date
        date = parser.parse(date)
        formatted_date = date.strftime("%Y-%m-%d")

        #Get Description
        info_margin_elements = soup.find_all(class_="information margin-bottom-xs-64")
        body = [element.text.strip() for element in info_margin_elements]
        markdown = ""
        for item in body:
            markdown += "- " + item.strip() + "\n\n"

        # Get Description
        pattern = r'<p class="desc preamble">(.*?)</p>'
        matches = re.findall(pattern, response.text, re.DOTALL)
        cleaned_text = [re.sub(r'<.*?>', '', match) for match in matches]
        description = cleaned_text[0].split('.')[0].strip()

        # Find the Google Maps link
        google_maps_link = soup.find("a", href=lambda href: href and "maps.google.com" in href)

        # Extract the href attribute value
        if google_maps_link:
            google_maps_link = google_maps_link["href"]
            lat_lng = google_maps_link.split('=')[1]
            embed_link = f'<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12345.6789!2d{lat_lng.split(",")[1]}!3d{lat_lng.split(",")[0]}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2z{lat_lng.split(",")[0]}!5e0!3m2!1sen!2sus!4v1234567890" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>'

        return {
            'title': title,
            'date': formatted_date,
            'description': description,
            'price': price,
            'google': embed_link,
            'location': place,
            'register': url,
            'body': markdown,
            'month': month,
        }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# Create Post
def generate_file(data, template_file, output_dir, id):
    try:
        # Check if data is None (indicating an error during extraction)
        if data is None:
            print("Skipping file generation due to extraction error.")
            return

        with open(template_file, 'r') as file:
            template = file.read()

        output = template.format(**data)

        location_section = "## Location\n" + data['google']
        output = output.replace("## Location", location_section)

        register_section = "## Sign Up\n" + data['register']
        output = output.replace("## Sign Up", register_section)

        body_section = "## Description\n" + data['body']
        output = output.replace("## Description", body_section)

        formatted_title = re.sub(r'\W+', '-', data['title'].lower().strip())
        output_file = f"{output_dir}/{id}-{formatted_title}.md"

        with open(output_file, 'w') as file:
            file.write(output)

        print(f"Output file created: {output_file}")

    except Exception as e:
        print(f"Error generating file: {e}")

# Catch no URL error
if len(sys.argv) < 2:
    print("Please provide the text file containing URLs as a command-line argument.")
    sys.exit(1)

# Read URLs from the text file
file_path = sys.argv[1]
with open(file_path, 'r') as url_file:
    urls = url_file.read().splitlines()

template_file = 'src/templates/template.md'
output_dir = 'content/posts'

for url in urls:
    digits = re.findall(r'\d+', url)
    id = digits[-1]

    data = extract_data(url)
    generate_file(data, template_file, output_dir, id)
