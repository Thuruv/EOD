from twill import *
from bs4 import BeautifulSoup
mybrowser = get_browser()
m1 = ['http://www.groupon.com/deals/gg-womens-stretch-skinny-jeans-1','http://www.groupon.com/deals/superdawg-drive-in-1-3']
for i in m1:
    mybrowser.go(i)
    soup = BeautifulSoup(mybrowser.get_html())
    try:
        mydivs = soup.find("div", class_= "buy long").text
    #mydivs = soup.find("div", id_= "deal-hero-price").text
        print mydivs.strip()
    except :
        print 'buy'
