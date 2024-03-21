import requests
from bs4 import BeautifulSoup

# Wikipedia link for List of Nobel Memorial Prize laureates in Economics
url = 'https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economics'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the Nobel laureates
table = soup.find('table', class_='wikitable')

# Loop through each row in the table and print the data
for row in table.find_all('tr'):
    # Extract data from each cell in the row
    cells = row.find_all('td')
    if len(cells) > 0:
        year = cells[0].text.strip()
        laureate = cells[1].text.strip()
        citation = cells[2].text.strip()
        print(f'Year: {year}, Laureate: {laureate}, Citation: {citation}')

