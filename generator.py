import sys
import requests
from bs4 import BeautifulSoup
import re

# Function to extract data from the webpage
def extract_data(url):
    # Send a GET request to the webpage
    response = requests.get(url)
    response.raise_for_status()  # Check for any errors

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the desired data using appropriate selectors
    title = soup.select_one('.cover-heading h1').get_text()
    date = soup.select_one('.item.date.event.hidden-xs strong').get_text()

    # Extract the href link from the button
    navbar_header = soup.select_one('.navbar-header')  # Select the div with class "navbar-header"
    button = navbar_header.select_one('.btn.btn-secondary.navbar-btn.text-xs-center')  # Select the button with the specified class
    register = button['href'] if button else ''

    # Return the extracted data as a dictionary
    return {
        'title': title,
        'date': date,
        'register': register,
    }

# Function to generate the file using the extracted data and template
def generate_file(data, template_file, output_dir):
    with open(template_file, 'r') as file:
        template = file.read()

    # Replace placeholders in the template with the extracted data
    output = template.format(**data)

    # Format the title for the output file name
    formatted_title = re.sub(r'\W+', '-', data['title'].lower().strip())

    # Construct the output file name
    output_file = f"{output_dir}/{formatted_title}.md"

    # Write the generated output to the file
    with open(output_file, 'w') as file:
        file.write(output)

    print(f"Output file created: {output_file}")

# Example usage
if len(sys.argv) < 2:
    print("Please provide the URL as a command-line argument.")
    sys.exit(1)

url = sys.argv[1]
template_file = 'src/templates/template.md'
output_dir = 'content/posts'

# Extract data from the webpage
data = extract_data(url)

# Generate the file using the extracted data and template
generate_file(data, template_file, output_dir)
