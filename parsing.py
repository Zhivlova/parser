import csv
import json
from collections import ChainMap
import requests
from bs4 import BeautifulSoup
import urllib.request


def get_data(url):
    """Получаем код странцицы"""
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/103.0.0.0 Safari/537.36 "
    }

    req = requests.get(url, headers=headers)
    src = req.text

    """Сохраняем код страницы"""
    with open("dejatelnost-gosudarstvennykh-institutov.html", "w") as file:
        file.write(src)

    with open("dejatelnost-gosudarstvennykh-institutov.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    all_data = {}

    try:
        """название опроса"""
        name_of_survey = soup.find(class_="h2-main")
        for name in name_of_survey:
            all_data['name_of_survey'] = name_of_survey.text.strip()

        """описание опроса"""
        description_of_survey = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find("p")
        for desc in description_of_survey:
            title = description_of_survey.text.strip()
            all_data['description_of_survey'] = description_of_survey.text.strip()

        """варианты ответа"""
        answer_options = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find_all("li")
        president = answer_options[0].text
        prime_minister = answer_options[1].text
        governments = answer_options[2].text
        duma = answer_options[3].text
        federation = answer_options[4].text

        for answer in answer_options:
            all_data['answer_options'] = answer.text
            print(all_data)

        """ссылки на скачивание"""
        all_download_links = soup.find_all(class_="ce-uploads")
        for link in all_download_links:
            table_link = 'https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov' + link.find('a').get(
                'href')
            # table_link_1 = table_link[0]
            # table_link_2 = table_link[1]

            all_data['all_download_links'] = table_link
            all_data['all_download_links'] = table_link

    except TypeError as e:
        print(f" [TypeError]: {e.strerror}, filename: {e.filename}")
    else:
        print("Writing to file...")

        with open('all_data.csv', "w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(name_of_survey)

        with open('all_data.csv', "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(title)

        with open('all_data.csv', "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (president,
                 prime_minister,
                 governments,
                 duma,
                 federation
                 )
            )

        with open('all_data.csv', "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    table_link,
                    table_link
                )
            )


print("Program started")
print(get_data("https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov/"))
print("Program finished")


url = 'https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov/fileadmin/user_upload/ratings/state_institutions.xlsx'
urllib.request.urlretrieve(url, 'cat.jpg')
