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
    title_element = soup.find('h2', class_='margin-xs-0 flex-grow-1')
    title = title_element.get_text() if title_element else "Placeholder Title"
    
    date_element = soup.find('strong', class_='info')
    date = date_element.get_text() if date_element else "Placeholder Date"

    # Take the URL and add /register to the end
    register = url + '/register'

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
