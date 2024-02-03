import os
import re
from datetime import datetime

# Define the directory containing the markdown files
directory = 'content/posts'

# Get the current date
current_date = datetime.now().date()

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):  # Check if the file is a markdown file
        filepath = os.path.join(directory, filename)
        
        # Read the content of the file
        with open(filepath, 'r') as file:
            content = file.read()
            
            # Search for the date key and extract its value
            match = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', content)
            if match:
                file_date = datetime.strptime(match.group(1), '%Y-%m-%d').date()
                
                # Check if the date is in the past
                if file_date < current_date:
                    os.remove(filepath)  # Remove the file
                    print(f"Removed {filename} as its date is in the past.")
