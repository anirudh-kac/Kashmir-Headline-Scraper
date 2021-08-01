from selenium import webdriver
from bs4 import BeautifulSoup

BASE_URL = "https://www.greaterkashmir.com/collection/top-stories"

driver = webdriver.Firefox()

def scraper():
    driver.get(BASE_URL)
    soup = BeautifulSoup(driver.page_source,"html5lib")

    headlines = soup.find_all('h6')

    print(headlines)

    for headline in headlines:
        print(headline.get_text())
        print()
        print("-------------------------------------------------------------------------")

    ##print(soup.prettify())



