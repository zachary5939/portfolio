import requests
from bs4 import BeautifulSoup
import re

def decode_message(doc_url):
    # Fetch the content from the Google Doc
    response = requests.get(doc_url)
    data = response.text

    # Parse the HTML content
    soup = BeautifulSoup(data, 'html.parser')

    # Extract table rows
    rows = soup.find_all('tr')

    coordinates = []
    max_x = 0
    max_y = 0

    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        if len(cols) == 3:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            coordinates.append((x, y, char))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

    # Debug print for parsed coordinates
    print("Parsed coordinates:")
    for coord in coordinates:
        print(coord)

    # Create the grid
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill the grid with characters
    for x, y, char in coordinates:
        grid[y][x] = char

    # Print the grid
    print("\nGrid:")
    for row in grid:
        print("".join(row))

# Example usage
decode_message('https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub')
