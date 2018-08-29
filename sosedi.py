import requests
from bs4 import BeautifulSoup


url = 'https://sosedi.by/o_nas/naydi_svoih_sosedey/'
path = r'C:\Users\Power Bi\Desktop\sosedi.csv'

def get_html(url):
    response = requests.get(url)
    return response.text


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    # table = soup.find_all('span', class_="adrs")
    table = soup.find('div', class_="findul")
    table2 = table.findAll('div', class_=["oneofthem", "zagolovok2"])

    # print(str(list(table2[0])[1]))
    #, class_=["oneofthem","zagolovok2"]
    with open(path, 'w') as file:
        file.write('ТипМагазина'+";"+ 'Магазин'+";"+'ПолныйАдрес'+";"+"НаселПункт"+";"+'\n')
    ci = ''
    addr = ''
    type_store = ''
    for i in range(len(list(table2))):

        if str(list(table2[i])[1]) == '<span class="oprfir"></span>':
            # print(table2[i].find('h2').text)
            ci = table2[i].find('h2').text
        else:
            # print(table2[i].find('span', class_="adrs").text)
            addr = table2[i].find('span', class_="adrs").text

            if addr.find('Соседи Экспресс')>0:
                type_store = 'Соседи Экспресс'
                addr = ','.join(addr.split('-')[:-1])
            else:
                type_store = 'Магазин'


        with open(path, 'a') as file:
            if addr != '':
                file.write(type_store+";"+'Соседи'+";"+ci+', '+addr+";"+addr+";"+'\n')
                addr = ''




    # for t in table2:
    #     rows = t.find('h2').text
    #     print(rows)
    #     for t1 in  table.find_all('div', class_="oneofthem"):
    #         s = t1.find('span', class_="adrs").text
    #         print(s)
        # l = s.split(",")
        # print(l)
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


