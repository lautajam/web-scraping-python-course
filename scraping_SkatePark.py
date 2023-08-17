from bs4 import BeautifulSoup
import requests

# HTML obtain
URL_BASE = 'https://scrapepark.org/courses/spanish/'
request_obtained = requests.get(URL_BASE)
html_obtained = request_obtained.text

#Parser HTML
soup = BeautifulSoup(html_obtained, 'html.parser')

#find() method
first_h2 = soup.find('h2')
print(first_h2)

# 46:59 https://www.youtube.com/watch?v=yKi9-BfbfzQ