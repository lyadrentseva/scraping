# http://beautiful-soup-4.readthedocs.io/en/latest/#parsing-only-part-of-a-document
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

url = 'http://www.bigzz.by/pages/Kontakti/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
# print(page.text)

name_list_items = soup.find_all('p')
# print(name_list_items[20:-2])


def main():
    print(parse(get_html(url)))

def get_html(url):
    response = requests.get(url)
    return response.text
# html = get_html(url)

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    # table = list(soup.find_all('div', class_='box-content box-category'))
    # table = list(soup.find_all('span', style_='font-family: &quot;Trebuchet MS&quot;, sans-serif; font-size: 14px'))
    table = list(soup.find_all('tbody'))[-1]
    print(len(table))
    return table


if __name__ == '__main__':
    main()
