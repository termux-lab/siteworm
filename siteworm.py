import requests
import re, os
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
os.system("clear")
print("""
\033[31m
\033[31m                       |
\033[31m                  ____/|____
\033[31m             .---':.:.''    '--.
\033[31m            /:.:..:....         '\.
\033[31m           |::.::.:....           |
\033[31m           |::.:.:::...           |
\033[31m           |:..::::. ..           |
\033[31m           |::.::....\033[32m[SITE]\033[31m       /
\033[33m    oo\033[31m      \:..:....:...        '
\033[33m    |" \033[31m      \.:..:....        .'
\033[33m    |\033[31m         `\:.:.:...     ./
\033[33m----'\033[31m           '--,-/|\----'\033[0m
WORMsite
                                 Termux-Lab | t.me/termuxlab

""")
href=[]
link0=[]
i = 0
q = 0
print("Укажи ссылку на сайт")
url = input("worm-> ")
html = requests.get(url).text
print()
print("\033[33mПоиск в [\033[32m", url, "\033[33m]\033[0m")
print("                <===>")
print()
links = re.findall('"((https|ftp)s?://.*?)"', html)
resp = requests.get(url)
http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
encoding = html_encoding or http_encoding
soup = BeautifulSoup(resp.content, "html.parser")
for link in soup.find_all('a', href=True):
    href.append(link['href'])
    print("\033[35mНашли\033[33m", link['href'], "\033[0m")
for link in soup.find_all('link', href=True):
    href.append(link['href'])
    print("\033[35mНашли\033[33m", link['href'], "\033[0m")
for link in soup.find_all('script', src=True):
    href.append(link['src'])
    print("\033[35mНашли\033[33m", link['src'], "\033[0m")
for link in soup.find_all('form', action=True):
    href.append(link['action'])
    print("\033[35mНашли\033[33m", link['action'], "\033[0m")
while True:
    try:
        link0.append(links[i][0])
        print("\033[35mНашли\033[33m", links[i][0], "\033[0m")
        i+=1
    except:
        break

for q in range(len(href)-1):
    try:
        html = requests.get(href[p]).text
        print()
        print("\033[33m---| Поиск в [\033[32m", href[p], "\033[33m]\033[0m")
        print("                   <===>")
        print()
    except:
        html = requests.get(url+"/"+href[q]).text
        print("")
        print("\033[33m---| Поиск в [\033[32m", url+"/"+href[q], "\033[33m]\033[0m")
        print("                   <===>")
        print()
    try:
        resp = requests.get(url+"/"+href[q])
    except:
        resp = requests.get(href[q])
    links111 = re.findall('"((https|ftp)s?://.*?)"', html)
    http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, "html.parser")
    try:
        for link222 in soup.find_all('a', href=True):
            print("\033[35m---| Нашли\033[33m", link222['href'], "\033[0m")
    except:
        pass
    try:
        for link222 in soup.find_all('link', href=True):
            print("\033[35m---| Нашли\033[33m", link222['href'], "\033[0m")
    except:
        pass
    try:
        for link222 in soup.find_all('script', src=True):
            print("\033[35m---| Нашли\033[33m", link222['src'], "\033[0m")
    except:
        pass
    try:
        for link in soup.find_all('form', action=True):
            print("\033[35m---| Нашли\033[33m", link222['action'], "\033[0m")
    except:
        pass

    for ii in range(len(links111)-1):
        try:
            print("\033[35m---| Нашли\033[33m", links111[i][0], "\033[0m")
            ii+=1
        except:
            pass
