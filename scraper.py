#We'll scrape headlines from a news website like BBC News

import requests
from bs4 import BeautifulSoup
import csv


# URL of the website to scrape
url = 'https://www.bbc.com/news'

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the elements that contain the headlines
headlines = soup.find_all('h3')

# Open a CSV file to write the scraped data
with open('headlines.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline'])  # Write the header row
    
    # Write each headline to the CSV file
    for headline in headlines:
        writer.writerow([headline.get_text(strip=True)])

print('Headlines have been successfully scraped and saved to headlines.csv')
