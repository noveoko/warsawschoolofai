import requests
from bs4 import BeautifulSoup as bs

base_url = 'theschool.ai'

def getAllBaseUrlLinks(base_url):
    #get the raw data from base_url
    response = requests.get(base_url)
    #check to make sure that the page response is acceptable
    if response.status_code == 200:
        #assign the value of the binary HTML response to raw_html
        raw_html = response.content
        #convert raw_html to a soup object for parsing
        soup = bs(raw_html, 'html.parser')
        #fetch all of the links from the page
        links = soup.find_all("a")
        #for every link found add it to the set unique_links
        unique_links = set(links)
        #return the set of unique links
        return unique_links

        
