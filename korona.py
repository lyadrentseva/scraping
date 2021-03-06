# http://beautiful-soup-4.readthedocs.io/en/latest/#parsing-only-part-of-a-document
import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.korona.by/shops/'
path = r'C:\Users\Power Bi\Desktop\korona.csv'

def get_html(url):
    response = requests.get(url)
    return response.text


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_="shop-list")
    rows = soup.find_all('div', class_="shop-list-item")
    # print(rows)
    # print(len(rows))
    # with open(path, 'w') as file:
    #     file.write('ТипМагазина'+";"+ 'Магазин'+";"+'ПолныйАдрес'+";"+"НаселПункт"+";"+"улица"+";"+"дом"+";"+'\n')
    for i in range(len(rows)):
        s = rows[i]
        # print(s)

        print(s.find_all('div', class_="shop-list-item-title-heading"))
        print(s.find_all('div', class_="shop-list-item-title-subheading small"))
        break
        # l = s.split(",")
    #     with open(path, 'a') as file:
    #         if len(l)>2:
    #             file.write('Магазин'+";"+'Брусничка'+";"+str(s)+";"+str(l[0])+";"+str(l[1])+";"+str(l[2])+";"+'\n')
    #         else:
    #             file.write('Магазин'+";"+'Брусничка'+";"+str(s)+";"+str(l[0])+";"+""+";"+str(l[1])+";"+'\n')
    #

def main():
    parse(get_html(url))

if __name__ == '__main__':
    main()


