import requests
from bs4 import BeautifulSoup
import googletrans

# Get the webpage
url = 'https://www.example.com/'
response = requests.get(url)

# Parse the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all the headers
headers = soup.find_all('h1', 'h2', 'h3', 'h4', 'h5', 'h6')

# Translate the headers to Spanish
translator = googletrans.Translator()
spanish_headers = []
for header in headers:
    spanish_headers.append(translator.translate(header.text, dest='es').text)

# Save the result into an HTML file
with open('result.html', 'w') as f:
    f.write('<html>\n')
    for header in spanish_headers:
        f.write('<h1>{}</h1>\n'.format(header))
    f.write('</html>')