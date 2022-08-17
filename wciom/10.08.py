from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def find_download_buttons(url):
    buttons = set()
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), "lxml")

    """получаем описание"""
    text = []
    description_of_survey = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find("p")
    description = description_of_survey.text.strip()
    text.append(description)

    if not text:
        question_of_survey = soup.find(class_="frame frame-default frame-type-html frame-layout-0").find("p")
        question = question_of_survey.text.strip()
        text.append(question)

        if not text:
            answer_options = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find_all("li")
            for answer in answer_options:
                answers = answer.text.strip()
                text.append(description)


    """получаем ссылку на скачивание"""
    all_download_links = soup.find_all(class_="ce-uploads")
    for link in all_download_links:
        table_link = 'https://wciom.ru' + link.find('a').get(
            'href')
        buttons.add(table_link)
        print(buttons)


    buttons_dict = {
        'text': text, 'buttons': buttons
    }
    return buttons_dict


print(find_download_buttons('https://wciom.ru/ratings/protestnyi-potencial'))
print('----------------------------------------------------')


def download_from_buttons(buttons_dict):
    """скачиваем данные по ссылкам"""
    try:
        buttons = buttons_dict.get('buttons')
        for i in buttons:
            filename = i.split('/')[-1]
            filename = 'wciom' + '_' + filename
            r = requests.get(i, allow_redirects=True)
            open(filename, "wb").write(r.content)
            print(f"{filename} from {i} - Download complete")
    except:
        print(f"{filename} from {i} - Download false")


download_from_buttons(find_download_buttons('https://wciom.ru/ratings/protestnyi-potencial'))
