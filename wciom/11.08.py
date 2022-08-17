from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import ssl


class WciomScraper:
    """
    Класс для извлечения данных со страниц wciom.ru
    """
    ssl._create_default_https_context = ssl._create_unverified_context  # устраняет ошибку ssl сертификата

    def find_download_buttons(url):
        html = urlopen(url)
        soup = BeautifulSoup(html.read(), "lxml")

        """получаем описание"""
        text = {}
        try:
            description_of_survey = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find("p")
            description = description_of_survey.text.strip()
            text['desc'] = description
        # TODO запись в логи
        except Exception:
            pass

        try:
            question_of_survey = soup.find(class_="frame frame-default frame-type-html frame-layout-0").find("p")
            question = question_of_survey.text.strip()
            text['quest'] = question
        # TODO запись в логи
        except Exception:
            pass

        try:
            answer_options = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find_all("li")
            for answer in answer_options:
                answers = answer.text.strip()
                text['answ'] = answers
        # TODO запись в логи
        except Exception:
            pass

        """получаем ссылку на скачивание"""
        buttons_dict = {}
        buttons = []
        try:
            all_download_links = soup.find_all(class_="ce-uploads")
            for link in all_download_links:
                table_link = 'https://wciom.ru' + link.find('a').get(
                    'href')
                buttons.append(table_link)
        # TODO запись в логи
        except Exception:
            pass

        buttons_dict = {
            'text': text, 'buttons': list(set(buttons))
        }

        try:
            buttons = buttons_dict.get('buttons')
            for button in buttons:
                filename = button.split('/')[-1]
                filename = 'wciom' + '_' + filename
                r = requests.get(button, allow_redirects=True)
                # TODO именование файлов
                open(filename, "wb").write(r.content)
                print(f"{filename} from {button} - Download complete")
        # TODO запись в логи
        except Exception:
            print(f"{filename} from {button} - Download false")


