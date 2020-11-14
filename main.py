from bs4 import BeautifulSoup as bs
import requests
from colorama import Fore, init, Style
import os

init(autoreset=True)
clear = lambda: os.system('cls')
clear()

url = 'https://rl.insider.gg/en/pc'
r = requests.session()


def get_content(html):
    soup = bs(html, 'html.parser')
    try:
        answer = soup.find_all('div', class_="itemNameSpan")
        return answer
    except:
        return None

while True:
    html = r.get(url)
    print('\n')
    name = input('Введите название предмета: ')
    clear()
    if html.status_code == 200:
        for item in get_content(html.text):
            if len(name.split(' ')) > 1:
                    if item.text.lower() == name.lower():
                        print("\n" + Fore.GREEN + item.parent.parent.parent.parent.parent.find_all('h2', class_='tableHeader')[0].text)
                        print(Fore.GREEN + item.text + ":\n")
                        for i, n in enumerate(item.parent.parent.find_all('td', class_="priceRange")):
                            s = 0
                            for k in n['class']:
                                if k == 'invisibleColumn':
                                    s = 1
                            if s == 0:
                                if n.text.replace('&hairsp', "") == "—":
                                    print(n['class'][0].replace("price", "") + ' ' + Fore.RED + n.text.replace('&hairsp', ""))
                                else:
                                    print(n['class'][0].replace("price", "") + ' ' + Style.BRIGHT + Fore.MAGENTA + n.text.replace('&hairsp', ""))
            else:
                for ittem in item.text.split(' '):
                    if ittem.lower().startswith(name.lower()):
                        print("\n" + Fore.GREEN + item.parent.parent.parent.parent.parent.find_all('h2', class_='tableHeader')[0].text)
                        print(Fore.GREEN + item.text + ":\n")
                        for i, n in enumerate(item.parent.parent.find_all('td', class_="priceRange")):
                            s = 0
                            for k in n['class']:
                                if k == 'invisibleColumn':
                                    s = 1
                            if s == 0:
                                if n.text.replace('&hairsp', "") == "—":
                                    print(n['class'][0].replace("price", "") + ' ' + Fore.RED + n.text.replace('&hairsp', ""))
                                else:
                                    print(n['class'][0].replace("price", "") + ' ' + Style.BRIGHT + Fore.MAGENTA + n.text.replace('&hairsp', ""))
    else:
        print('Сайт не дал ответа!')
