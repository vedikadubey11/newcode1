import requests  
from bs4 import BeautifulSoup  
  
# URL of the website to scrape  
url = "https://www.example.com"  
  
# Send a GET request to the website  
response = requests.get(url)  
  
# Parse the HTML content using BeautifulSoup  
soup = BeautifulSoup(response.content, 'html.parser')  
  
# Find the specific data you want to scrape (e.g. all links on the page)  
links = soup.find_all('a')  
  
# Print the results  
for link in links:  
   print(link.get('href'))
