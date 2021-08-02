import requests
from bs4 import BeautifulSoup
from datetime import date
from csv import writer

BASE_URL = 'https://kashmirobserver.net/news/top-stories/'


def scraper():
    res = requests.get(BASE_URL)
    soup = BeautifulSoup(res.text,"html5lib")
    headlines = soup.find_all('a',attrs={"rel" : "bookmark"})

    filename = str(date.today())

    file = open("./archives/kashmir_observer/" + filename + ".csv",'w')
    csv_writer = writer(file)

    for headline in headlines:
        if(headline.get_text().strip()):
            print(headline.get_text().strip())
            csv_writer.writerow([headline.get_text().strip()])
            print("---------------------------------------------")

    file.close()