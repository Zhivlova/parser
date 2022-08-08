import requests

link = 'https://wciom.ru/fileadmin/user_upload/ratings/state_institutions.xlsx'

def save_from_www(link):
    filename = link.split('/')[-1]
    print(filename)
    r = requests.get(link, allow_redirects=True)
    open(filename, "wb").write(r.content)

save_from_www(link)