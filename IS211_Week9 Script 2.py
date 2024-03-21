import requests
from bs4 import BeautifulSoup

# Wikipedia link for List of NBA champions
url = 'https://en.wikipedia.org/wiki/List_of_NBA_champions'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the NBA champions
table = soup.find('table', class_='wikitable')

# Loop through each row in the table and print the data
for row in table.find_all('tr'):
    # Extract data from each cell in the row
    cells = row.find_all('td')
    if len(cells) > 0:
        year = cells[0].text.strip()
        champion = cells[1].text.strip()
        runner_up = cells[2].text.strip()
        series_result = cells[3].text.strip()
        print(f'Year: {year}, Champion: {champion}, Runner-up: {runner_up}, Series Result: {series_result}')

