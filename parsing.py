import json
import requests
from bs4 import BeautifulSoup


# """Получаем код странцицы"""
#
# url = "https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov/"
#
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
# #print(src)
#
# """Сохраняем код страницы"""
#
# with open("dejatelnost-gosudarstvennykh-institutov.html", "w") as file:
#     file.write(src)

with open("dejatelnost-gosudarstvennykh-institutov.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

"""название опроса"""
name_of_survey = soup.find(class_="h2-main")
print(name_of_survey.text.strip())

"""описание опроса"""
description_of_survey = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find("p")
print(description_of_survey.text.strip())

"""варианты ответа"""
answer_options = soup.find(class_="frame frame-default frame-type-text frame-layout-0").find_all("li")
# print(answer_options)
for item in answer_options:
    print(item.text.strip())

"""ссылка на скачивание"""


all_download_links = soup.find_all(class_="ce-uploads")
all_download_files_dict = {}

for item in all_download_links:
    item_text = item.text.strip()
    item_href = item.get("a")

    all_download_files_dict[item_text] = item_href

with open("all_download_files.json", "w") as file:
    json.dump(all_download_files_dict, file, indent=4, ensure_ascii=False)

with open("all_download_files.json") as file:
    all_download_files = json.load(file)

for file_name, file_href in all_download_files.items():
    rep = [",", " ", "-"]
    for item in rep:
        if item in file_name:
            file_name = file_name.replace(item, "_")

# all_download_links = soup.find(class_="ce-uploads").find_all("href")
# all_download_files_dict = {}
#
# for item in all_download_links:
#     item_text = item.text
#     item_href = item.get("href")
#
#     all_download_files_dict[item_text] = item_href
#
# with open("all_download_files.json", "w") as file:
#     json.dump(all_download_files_dict, file, indent=4, ensure_ascii=False)
#
# with open("all_download_files.json") as file:
#     all_download_files = json.load(file)
#
# for file_name, file_href in all_download_files.items():
#     rep = [",", " ", "-"]
#     for item in rep:
#         if item in file_name:
#             file_name = file_name.replace(item, "_")