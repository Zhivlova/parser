import requests
from bs4 import BeautifulSoup
import os
import ssl

link = 'https://wciom.ru/ratings/indeks-potrebitelskogo-doverija'

def save_from_www(link):
    filename = link.split('/')[-1]
    print(filename)
    r = requests.get(link, allow_redirects=True)
    open(filename, "wb").write(r.content)

save_from_www(link)

# r = requests.get(url_to_the_file)
#
# with open('xl.xlsx', 'wb') as f:
#     f.write(r.content)
#
# def get_xl_files(data_):
#     links = []
#     names_of_xl_files = []
#     for link in data_:
#         if ".xlsx" in link['href']:
#             print(link['href'])
#             links.append(link['href'])
#             names_of_xl_files.append(link.text)
#
#     if len(names_of_xl_files) == 0:
#         raise Exception
#
#     else:
#         for place in links:
#             with open(names_of_xl_files[place], 'wb', encoding="Windows-1251") as f:
#                 content = requests.get(links[place]).content
#                 f.write(content)
#
# url = 'https://wciom.ru/fileadmin/user_upload/ratings/state_institutions.xlsx'
# result = requests.get(url).content
# soup = BeautifulSoup(result, 'html.parser')
# data = soup.find_all('a')
# get_xl_files(data)
