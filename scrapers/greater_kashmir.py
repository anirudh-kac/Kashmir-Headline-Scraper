from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
from csv import writer
BASE_URL = "https://www.greaterkashmir.com/collection/top-stories"

def scraper():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    soup = BeautifulSoup(driver.page_source,"html5lib")
    driver.close()
    headlines = soup.find_all('h6')

    filename = str(date.today())

    file = open("./archives/greater_kashmir/" + filename + ".csv",'w')
    csv_writer = writer(file)
    for headline in headlines:
        csv_writer.writerow([headline.get_text()])
        print(headline.get_text())
        print()
        print("-------------------------------------------------------------------------")

    file.close()
    ##print(soup.prettify())



