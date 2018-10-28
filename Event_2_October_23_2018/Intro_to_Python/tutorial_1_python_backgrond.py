import requests, os
from bs4 import BeautifulSoup as bs

#selenium webdriver imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def fetchLinksUsingSelenium(base_url):
    unique_links = set()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options)
    driver.get(base_url)
    driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        link = elem.get_attribute("href")
        unique_links.add(link)
        #print(link)
    return unique_links

def getAllBaseUrlLinks(base_url):
    unique_links = set()
    content_length = 0
    #get the raw data from base_url
    response = requests.get(base_url)
    #check to make sure that the page response is acceptable
    try:
        content_length = int(response.headers['Content-Length'])
    except KeyError as ke:
        print(ke)
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
            except Exception as ee:
                    #print the exception to the console
                    print(ee)
    #return the set of unique links
    elif content_length < 3000:
        print("Fetching Content Using SELENIUM")
        #fetch page using Selenium
        links = fetchLinksUsingSelenium(base_url)
        for link in links:
            unique_links.add(link)
    else:
        pass
    return unique_links

def fetchLinksFromListOfUrls(base_url, allurls="output/allurls.txt"):
    list_of_urls = getAllBaseUrlLinks(base_url)
    with open(allurls, 'w') as urlfile:
        for top_link in list_of_urls:
            try:
                sub_links = getAllBaseUrlLinks(top_link)
                for sub_link in sub_links:
                    #print the base_url and then the sub_link
                    result = f"{top_link}\t{sub_link}\n"
                    print(result)
                    urlfile.write(result)
            except Exception as ee:
                print(ee)

def addUniqeLinksToFile(base_url, link_file="output/unique_links.txt"):
    #open link_file as a file object using with
    with open(link_file, 'w') as outfile:
        #fetch all the links
        sitelinks = getAllBaseUrlLinks(base_url)
        for link in sitelinks:
                #for every unique link print it to a new line
                outfile.write(f"{link}\n")

def app(base_url):
    #fetch all unique links and print them to a file
    #fetchLinksFromListOfUrls(base_url)
    #getAllBaseUrlLinks(base_url)
    fetchLinksUsingSelenium(base_url)

#allow this code to be imported as a module
if __name__ == "__main__":
    app("https://theschool.ai")
