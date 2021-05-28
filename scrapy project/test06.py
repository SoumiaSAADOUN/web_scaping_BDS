import requests
import json

# the user enters the url of the webpage to crawl
url =input()
# we send a get request to get the page's content
content= requests.get(url)



