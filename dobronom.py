import re
import requests
from bs4 import BeautifulSoup

url = 'http://dobronom.by/shops/'
path = r'C:\Users\Power Bi\Desktop\dobronom.csv'

def get_html(url):
    response = requests.get(url)
    return response.text


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all('td', class_="mmliName")
    rows = ''

    # with open(path, 'w') as file:
    #     file.write('ТипМагазина'+";"+ 'Магазин'+";"+  'ПолныйАдрес'+";"+'\n')
    # for t in table:
    #     rows = t.find('a')
    #     with open(path, 'a') as file:
    #         file.write('Магазин'+";"+'Доброном'+";"+str(rows.text)+";"+'\n')


    with open(path, 'w') as file:
        file.write('ТипМагазина'+";"+ 'Магазин'+";"+'ПолныйАдрес'+";"+"НаселПункт"+";"+"улица"+";"+"дом"+";"+'\n')
    for t in table:
        rows = t.find('a')
        s = rows.text
        l = s.split(",")
        # print(l)
        with open(path, 'a') as file:
            if len(l) > 2:
                file.write('Магазин'+";"+'Доброном'+";"+str(s)+";"+str(l[0])+";"+str(l[1])+";"+str(l[2])+";"+'\n')
            # elif len(l) > 1 and len(l) < 3 :
            #     file.write('Магазин'+";"+'Брусничка'+";"+str(s)+";"+str(l[0])+";"+""+";"+str(l[1])+";"+'\n')
            else:
                file.write('Магазин'+";"+'Доброном'+";"+str(s)+";"+str(l[0])+";"+""+";"+""+";"+'\n')

def main():
    parse(get_html(url))

if __name__ == '__main__':
    main()
