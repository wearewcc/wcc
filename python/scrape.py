# from lxml import html
# #pip install --user lxml
# import requests
#
#
# page = requests.get('')
# tree = html.fromstring(page.content)
#
# print page.content
#
# #This will create a list of buyers:
# buyers = tree.xpath('//div[@class="ires"]/text()')
# #This will create a list of prices
# #prices = tree.xpath('//span[@class="item-price"]/text()')
#
#
# print 'Buyers: ', buyers
# #print 'Prices: ', prices
#

import requests
from bs4 import BeautifulSoup

#pip install --user bs4

sites = ['https://www.travelzoo.com/top20/', 'https://www.groupon.com/occasion/last-minute-travel-deals']

for site in sites:
    page = requests.get(site)

    if 'Costa Rica' in page.content:
        print 'Found Boston in ' + site



#soup = BeautifulSoup(page.content, 'html.parser')

#print soup.find(id="link3")
#print(soup.get_text())

#print(soup.prettify())
