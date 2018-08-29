
import requests
from bs4 import BeautifulSoup

url = 'http://www.martinn.by/ru/kontakty'
path = r'C:\Users\Power Bi\Desktop\Martin.csv'

def get_html(url):
    response = requests.get(url)
    print(response.text)
    return response.text


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    # table = soup.find('div', class_="panel")
    rows = soup.find_all('td',  class_="xl64")
    print(rows)
    # with open(path, 'w') as file:
    #     file.write('ТипМагазина'+";"+ 'Магазин'+";"+  'ПолныйАдрес'+";"+'\n')
    # for i in range(len(rows)):
    #     print(list(rows[i])[0])
    #     s = list(rows[i])[0]
    #     with open(path, 'a') as file:
    #         file.write('Магазин'+";"+'Брусничка'+";"+str(s)+";"+'\n')

def main():
    get_html(url)
    parse(get_html(url))

if __name__ == '__main__':
    main()

