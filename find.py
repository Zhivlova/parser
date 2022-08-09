import csv
from urllib.request import urlopen
from urllib.parse import urlparse, urljoin
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import ssl


url = 'https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov'

def url_is_valid(url):
    """Проверяет, является ли url допустимым"""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_links(url):
    """Возвращает все найденные URL-адреса на `url, того же веб-сайта"""
    internal_urls = set() # внутренние ссылки
    # external_urls = set() # внешние ссылки
    urls = set()
    #доменное имя URL без протокола
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        # if href == "" or href is None:
        #     # пустой тег href
        #     continue
        # if not url_is_valid(href):
        #     # недействительный URL
        #     continue
        # if domain_name not in href:
        #     # внешняя ссылка
        #     if href not in external_urls:
        #         external_urls.add(href)
        #     continue
        urls.add(href)
        # internal_urls.add(href)
        # external_urls.add(href)

    return urls
    print(urls)
    # print(external_urls)
    # print(internal_urls)
    # buttons = list()
    # for link in urls:

print(get_all_links('https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov'))



def save_from_www(urls):
    filename = urls.split('/')[-1]

    # r = requests.get(url, allow_redirects=True)
    # open(filename, "wb").write(r.content)










