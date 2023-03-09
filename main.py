from pprint import pprint

import requests

# Задача 1
# TODO: спарсить страницу с супергероями, Найти в ней трех конкретных героев, и выявить кто из них умнее.
set = []
superheroes = ['Hulk', 'Captain America', 'Thanos']
superheroes_int = {}


def super_heroes():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url=url)
    set.append(response.json())
    for s in set[0]:
        for hero_name in superheroes:
            if hero_name == s['name']:
                superheroes_int[hero_name] = s['powerstats']['intelligence']

    sorted_heroes = sorted(list(superheroes_int.items()), reverse=True)
    return f'Cамый умный супергерой, это {sorted_heroes[0][0]}, его интеллект - {sorted_heroes[0][1]} cупергеройских очков'


# Задача 2
# TODO: Написать прогу, которая забирает с компа файл и отправляет его на Я.Диск

TOKEN = ''


class YandexDisk:


    def __init__(self, token):
        self.token = token
        self.yandex_url = 'https://cloud-api.yandex.net/'
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)

        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href_response = self.get_upload_link(disk_file_path=disk_file_path).get("href", "")
        href = href_response
        response = requests.put(url=href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print("Success")






if __name__ == '__main__':
    pprint(super_heroes(), sort_dicts=False)

    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk('netology/test', 'test.txt')


