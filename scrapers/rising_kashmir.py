from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
from csv import writer

BASE_URL = 'https://www.risingkashmir.com/category/Top-Stories'


def scraper():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    soup = BeautifulSoup(driver.page_source,"html5lib")
    driver.close()
    headlines = soup.find_all('h2',class_= "headline")

    filename = str(date.today())

    file = open("./archives/rising_kashmir/" + filename + ".csv",'w')
    csv_writer = writer(file)

    for headline in headlines:
        print(headline.get_text().strip())
        csv_writer.writerow([headline.get_text().strip()])
        print("---------------------------------------------")

    file.close()