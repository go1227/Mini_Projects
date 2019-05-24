# Package requirements:
# - BeautifulSoup4, requests, lxml

from bs4 import BeautifulSoup
import requests
import csv

# essential domain values
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

# SlickDeals.net
slickdeals_domain = 'http://www.slickdeals.net'
slickdeals_url = slickdeals_domain+'/video-game-deals/?page='

# Walmart.com
walmart_domain = 'https://www.walmart.com'
walmart_url = walmart_domain + '/browse/video-games/playstation-4-games/2636_1102672_1105671?page=_PAGE_POSITION_'

# CSV file
csv_file = open('videogame_offers.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product_Name', 'Price', 'Store_Name', 'Link'])


def pullslickdealsdeals(pages):
    for p in range(1, pages+1):
        source = requests.get(slickdeals_url + str(p), headers=agent).text
        soup = BeautifulSoup(source, 'lxml')

        for item in soup.find_all('div', class_='fpItem'):
            # Product Name
            try:
                product_name = item.find('a', class_='itemTitle').text
            except:
                product_name = 'Product Name Not Available'

            # Price
            try:
                price = item.find('div', class_='itemInfoLine')
                price = price.find('div', class_='priceLine').text.strip()
            except:
                price = 'Price Not Available'

            # Store Name
            try:
                store_name = item.find('span', class_='itemStore').text
            except:
                store_name = 'Store Name Not Available'

            # Link for the offer
            try:
                link = slickdeals_domain + item.find('a', class_='itemTitle')['href']
            except:
                link = 'Link Not Available'

            csv_writer.writerow([product_name, price, store_name, link])
            # print(f'\nResults: \n{store_name}\n{product_name}\n{price}\n{link}')


def pullwalmartdeals(pages):
    for p in range(1, pages+1):
        walmart_full_url = walmart_url.replace('_PAGE_POSITION_', str(pages))

        source = requests.get(walmart_full_url, headers=agent).text
        soup = BeautifulSoup(source, 'lxml')

        for match in soup.find_all('div', class_='search-result-gridview-item-wrapper'):
            try:
                price = match.find('div', class_='product-price-with-fulfillment')
                price = price.find('span', class_='price-group').text
            except:
                price = 'Price Not Available'

            try:
                link = walmart_domain + match.find('a', class_='product-title-link')['href']
            except:
                link = 'Link Not Available'

            try:
                product_name = match.find('a', class_='product-title-link')['aria-label']
            except:
                product_name = 'Product Name Not Available'

            store_name = 'Walmart (video-game section)'

            csv_writer.writerow([product_name, price, store_name, link])
            # print(f'\nResults: \n{store_name}\n{product_name}\n{price}\n{link}')


print('Pulling data from websites...')
pullslickdealsdeals(3)
pullwalmartdeals(3)
print('Done!')
