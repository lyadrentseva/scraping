# http://beautiful-soup-4.readthedocs.io/en/latest/#parsing-only-part-of-a-document
import csv
import requests
from bs4 import BeautifulSoup

url = 'http://raduga100.by/kontakty'
path = r'C:\Users\Power Bi\Desktop\raduga.csv'

def get_html(url):
    response = requests.get(url)
    return response.text


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_="content-inner")
    rows = soup.find_all('a', class_="accordion-toggle")
    print(table)
    # with open(path, 'w') as file:
    #     file.write('ТипМагазина'+";"+ 'Магазин'+";"+'ПолныйАдрес'+";"+"НаселПункт"+";"+"улица"+";"+"дом"+";"+'\n')
    # for i in range(len(rows)):
    #     s = list(rows[i])[0]
    #     l = s.split(",")
    #     with open(path, 'a') as file:
    #         if len(l)>2:
    #             file.write('Магазин'+";"+'Радуга-свет, г. Солигорск'+";"+str(s)+";"+str(l[0])+";"+str(l[1])+";"+str(l[2])+";"+'\n')
    #         else:
    #             file.write('Магазин'+";"+'Радуга-свет, г. Солигорск'+";"+str(s)+";"+str(l[0])+";"+""+";"+str(l[1])+";"+'\n')


def main():
    parse(get_html(url))

if __name__ == '__main__':
    main()


