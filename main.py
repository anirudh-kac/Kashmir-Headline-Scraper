import sys

from scrapers.greater_kashmir import scraper as gk_scraper
from scrapers.rising_kashmir import scraper as rk_scraper
from scrapers.kashmir_observer import scraper as ko_scraper

def main():

    if len(sys.argv)!=2 :
        print("Usage : python main.py gk | rk | ko")
        print("gk - Greater Kashmir")
        print("rk - Rising  Kashmir")
        print("ko - Kashmir Observer")
        return
    else:

        keyword = sys.argv[1]
        if keyword == "gk":
            gk_scraper()
        elif keyword =="rk":
            rk_scraper()
        elif keyword == "ko":
            ko_scraper()
        else:
            print("Invalid keyword")



if __name__ == "__main__":
    main()