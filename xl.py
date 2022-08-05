import re
import urllib
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys
import ssl
import requests
import shutil
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen('https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov')
soup = BeautifulSoup(html.read(), "lxml")
all_download_links = soup.find_all(class_="ce-uploads")
for link in all_download_links:
    table_link = link.find('a').get(
        'href')
    print(table_link)

f = open(r'xl', "wb")
ufr = requests.get('https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov' + table_link)
f.write(ufr.content)
f.close()

# href="/fileadmin/user_upload/ratings/state_institutions
