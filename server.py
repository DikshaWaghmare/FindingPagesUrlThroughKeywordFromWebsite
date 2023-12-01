# code to find all keywords in anchor tag for a given website#

from bs4 import BeautifulSoup
import requests

# Replace 'https://www.example.com' with the URL of the website you want to scrape
url = 'https://www.cricbuzz.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all anchor tags on the webpage
anchor_tags = soup.find_all('a')

# Extract keywords from the anchor tags
for tag in anchor_tags:
    # Get the text within the anchor tag
    text = tag.get_text()
    
    # You can perform further processing on the text to extract keywords
    # For instance, splitting the text into words to get individual keywords
    keywords = text.split()
    
    # Print the keywords
    print(f"Keywords in anchor tag: {keywords}")
