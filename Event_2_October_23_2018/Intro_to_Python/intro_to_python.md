# Intro to python
Instructor: Marcin Kraszewski

## Python Background
**20:00-20:07**
* What is **Python**?
* Which major companies use **Python**?
* How can I use Python if I'm not an engineer and don't work for a tech company?
* Isn't Excel good enough?
* What are some **amazing things anyone can build** using Python?

## Python Crash Course
**20:07-20:15**
* The **Zen of Python**
* What is a **variable**?
* What is a `list`?
* What is a `tuple`?
* What is a `set`?
* What is a `dict`?
* What is a **list comprehension**?
* What is a **function**?
* What is a **class**?
* Python Built-in String functions
 * `.upper()`
 * `.lower()`
 * `.title()`
 * `.isalpha()`

## Intro to Web scraping
**20:15-20:20**
* What is **web scraping**?
* What is an **API**?
* If API's exist why would I waste the time to write my own scraper?
* **Ethics** of webscraping
* Webscraping **Dangers**

## Don't reinvent the wheel
**20:20-20:30**
* What is a **library** in Python?
* How do I use a library?
* What are the pros and cons of using a library vs. writing a solution from scratch?

## Python Requests
**20:30-20:40**
* What is **Python Requests**
* How do I fetch a web page
* How do I set a `timeout`?
* How do I *disguise* myself as a browser session?

## Python + Selenium
**20:40-20:50**
* Requests vs. Selenium
* Open a browser
* Request a page
* Click a button

## HTML Parsing with Beautiful Soup
**20:50-21:00**
* What is **Beautiful Soup**?
* Extract all the headings in the page
* Extract all the links in the page
* Extract all the text from the page

## Build a Webscraper
**21:00-21:20**
* Write a web scraper that will do the following:
 * Visit a website
 * For every page on the website **save the HTML** and **extract the links** to a **text file**
 * Recursively visit pages until a **depth** is reached
* Deploy the script to PythonAnywhere
  * Set the script to run every 24 hours and send an email if any new local links are detected

## Next Steps
Take what you've learned tonight and create your own customized webscraping application to collect data that interests you.
* Use the **Flask** web framework to create a simple admin panel to easily control your scraping application. The application should have the following features:
* Set the script schedule (every 12 hours, every 24 hours, every week, or once per month)
* Set the base_url that the app will use when scraping

Post your code to Github so that we can discuss it at the next meeting. The 2 best projects (in terms of code quality and execution) will be featured on our Facebook page and mentioned at the next meeting.
