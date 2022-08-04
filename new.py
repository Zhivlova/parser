import json
import requests
from bs4 import BeautifulSoup


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
        for description in description_of_survey:
            all_data['description_of_survey'] = description_of_survey.text.strip()

        """варианты ответа"""
        answer_options = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find_all("li")
        for answer in answer_options:
            all_data['answer_options'] = answer.text

        """ссылки на скачивание"""
        all_download_links = soup.find_all(class_="ce-uploads")
        length = len(answer_options)
        n = 0
        while n < length:
            for link in all_download_links:
                table_link = 'https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov' + link.find('a').get('href')
                all_data['all_download_links'] = table_link
                n += 1
        print(all_data)
    except TypeError as e:
        print(f" [TypeError]: {e.strerror}, filename: {e.filename}")

    else:
        print("Writing to file...")
        iteration_count = int(len(all_data))
        count = 0
        while n < length:
            with open("all_data.json", "r+") as file:
                json.dump(all_data, file, indent=4, ensure_ascii=False)

            with open("all_data.json") as file:
                all_data = json.load(file)
                n += 1


print("Program started")
print(get_data("https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov/"))
print("Program finished")
