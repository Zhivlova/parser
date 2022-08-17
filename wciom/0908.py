from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import ssl
import csv

ssl._create_default_https_context = ssl._create_unverified_context


def find_download_buttons(url):
    buttons = set()
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), "lxml")
    all_download_links = soup.find_all(class_="ce-uploads")
    for link in all_download_links:
        table_link = 'https://wciom.ru' + link.find('a').get(
            'href')
        buttons.add(table_link)
        # возвращаем пронумерованный set()
        for index, value in enumerate(buttons, 1):
            print(index, value)
    return buttons

print(find_download_buttons('https://wciom.ru/ratings/indeks-potrebitelskogo-doverija'))


def download_from_buttons(url):
    filename = url.split('/')[-1]
    filename = 'wciom' + '_' + filename
    r = requests.get(url, allow_redirects=True)
    open(filename, "wb").write(r.content)
    print(f"{filename}  - Writing complete")

download_from_buttons(
    'https://wciom.ru/fileadmin/user_upload/ratings/pokupki_doverie.xls')


def get_title(url):
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), "lxml")
    name_of_survey = soup.find(class_="h2-main")
    for name in name_of_survey:
        title = name_of_survey.text.strip()
        print(title)
        return title


get_title('https://wciom.ru/ratings/indeks-potrebitelskogo-doverija')


def get_description(url):
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), "lxml")
    description_of_survey = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find("p")
    for desc in description_of_survey:
        description = desc.text.strip()
        print(description)
    return description


get_description('https://wciom.ru/ratings/indeks-potrebitelskogo-doverija')


def get_answer_options(url):
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), "lxml")
    answer_options = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find_all("li")
    for answer in answer_options:
        answers = answer.text.strip()
        print(answers)
        return answers


get_answer_options('https://wciom.ru/ratings/indeks-potrebitelskogo-doverija')

def write_to_csv():
    with open('1_wciom_indeks-potrebitelskogo-doverija', 'w') as file:
        file_csv = csv.writer(file)
        file_csv.writerows(title)
        file_csv.writerows(description)
        file_csv.writerows(answers)





