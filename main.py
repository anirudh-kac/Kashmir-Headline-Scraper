import sys

from scrapers.greater_kashmir import scraper as gk_scraper
from scrapers.rising_kashmir import scraper as rk_scraper
from scrapers.kashmir_observer import scraper as ko_scraper

from utils.help import print_help

def main():

    if len(sys.argv)!=2 :
        print("Usage : python main.py gk | rk | ko | help")

        print("help - Get Help")
        print("gk - Greater Kashmir")
        print("rk - Rising  Kashmir")
        print("ko - Kashmir Observer")
        return
    else:

        keyword = sys.argv[1]
        if keyword == "help":
            print_help()
        elif keyword == "gk":
            gk_scraper()
        elif keyword =="rk":
            rk_scraper()
        elif keyword == "ko":
            ko_scraper()
        else:
            print("Invalid keyword\n Run 'main.py help' to get help")



if __name__ == "__main__":
    main()