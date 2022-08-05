from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys
import ssl
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        soup = BeautifulSoup(html.read(), "lxml")
        name_of_survey = soup.find(class_="h2-main")
        for name in name_of_survey:
            title = name_of_survey.text.strip()
    except AttributeError as e:
        return None
    return title


title = get_title('https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov')
if title == None:
    print(f"Название не найдено")
else:
    print(title)


def get_description(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        soup = BeautifulSoup(html.read(), "lxml")
        description_of_survey = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find("p")
        for desc in description_of_survey:
            description = description_of_survey.text.strip()
    except AttributeError as e:
        return None
    return description


description = get_description('https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov')
if description == None:
    print(f"Описание не найдено")
else:
    print(description)


def get_answer_options(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        soup = BeautifulSoup(html.read(), "lxml")
        answer_options = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find_all("li")
        president = answer_options[0].text
        prime_minister = answer_options[1].text
        governments = answer_options[2].text
        duma = answer_options[3].text
        federation = answer_options[4].text
    except AttributeError as e:
        return None
    return president, prime_minister, governments, duma, federation


answer_options = get_answer_options('https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov')
if answer_options == None:
    print(f"Ответы не найдены")
else:
    print(answer_options)


def get_all_download_links(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        soup = BeautifulSoup(html.read(), "lxml")
        all_download_links = soup.find_all(class_="ce-uploads")
        for link in all_download_links:
            table_link = 'https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov' + link.find('a').get(
                'href')
            print(table_link)

    except AttributeError as e:
        return None
    return table_link


all_download_links = get_all_download_links('https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov')
if all_download_links == None:
    print(f"Ссылки на скачивание не найдены")
else:
    print(all_download_links)
