import requests
from bs4 import BeautifulSoup as bs

def getAllBaseUrlLinks(base_url):
    unique_links = set()
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
        #for every link found add `HREF` to unique_links
        for link in links:
            #try to extract the href from the link
            try:
                href = link['href']
                #add the href to the set of unique_links
                unique_links.add(href)
            #if that fails raise an exception
            except exception as ee:
                #print the exception to the console
                print(ee)
    #return the set of unique links
    return unique_links

def addUniqeLinksToFile(base_url, link_file="unique_links.txt"):
    #open link_file as a file object using with
    with open(link_file, 'w') as outfile:
        #fetch all the links
        sitelinks = getAllBaseUrlLinks(base_url)
        for link in sitelinks:
            #for every unique link print it to a new line
            outfile.write(f"{link}\n")

def app(base_url):
    #fetch all unique links and print them to a file
    addUniqeLinksToFile(base_url)


#allow this code to be imported as a module
if __name__ == "__main__":
    app("https://theschool.ai")
