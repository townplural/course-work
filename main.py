import requests
from pprint import pprint
from settings import vk_token


class VKontakte:
    """
    1)Получение информации о пользователе в ВК
    2)Получение списка фотографий
    3)Создание словаря (URL фотографии: количество лайков)
    4)Исправление имён если есть одинаковое количество лайков
    """

    dict_of_photos = {}
    list_of_likes = []
    dict_of_dates = {}
    list_of_repeats = []

    def __init__(self, token):
        self.token = token
        self.id = input('Введите id пользователя vk: ')

    def get_profile_photos(self):

        params = {
            'access_token': vk_token,
            'owner_id': self.id,
            'album_id': 'profile',
            'rev': '1',
            'extended': '1',
            'v': '5.131'
        }
        response = requests.get('https://api.vk.com/method/photos.get', params=params)
        dict_of_photo_info = response.json()
        for i in range(dict_of_photo_info['response']['count']):
            self.list_of_likes.append(dict_of_photo_info['response']['items'][i]['likes']['count'])
            self.dict_of_photos[dict_of_photo_info['response']['items'][i]['sizes'][-1]['url']] =\
                dict_of_photo_info['response']['items'][i]['likes']['count']
            self.dict_of_dates[dict_of_photo_info['response']['items'][i]['sizes'][-1]['url']] = \
                dict_of_photo_info['response']['items'][i]['date']
        pprint("Фотографии получены")

    def get_correct_names(self):

        for z in self.dict_of_photos:
            q = 0
            for x in range(len(self.list_of_likes)):
                if self.dict_of_photos[z] == self.list_of_likes[x]:
                    q += 1
                else:
                    pass
                if q > 1:
                    self.list_of_repeats.append(z)
        dict = {}
        for w in self.dict_of_dates:
            for e in self.list_of_repeats:
                if w == e:
                    dict[w] = self.dict_of_dates[w]

        for a in self.dict_of_photos:
            for s in dict:
                if a == s:
                    d = self.dict_of_photos[a]
                    self.dict_of_photos[a] = f"{dict[s]}, {d}"
        pprint('Фотографиям присвоены корректные имена')


class Yandex():

    """
    1) Передача Токена
    2)Получение Headers
    3)Создание папки и присвоение ей имени
    4)Загрузка фото на яндекс диск
    """

    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token
        self.folder_name = input('Введите имя папки: ')

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self):
        path = self.folder_name
        uri = 'v1/disk/resources'
        request_url = self.base_host + uri
        res = requests.put(f'{request_url}?path={path}', headers=self.get_headers())
        pprint("Папка создана")
        return

    def upload_from_internet(self):
        for url in VKontakte.dict_of_photos:
            uri = 'v1/disk/resources/upload/'
            request_url = self.base_host + uri
            yandex_path = '/' + f'{self.folder_name}/' + f"{VKontakte.dict_of_photos[url]}" + '.jpg'
            params = {'url': url, 'path': yandex_path}
            res = requests.post(request_url, params=params, headers=self.get_headers())
            pprint('Фотография добавлена')


if __name__ == '__main__':
    vk = VKontakte(vk_token)
    vk.get_profile_photos()
    vk.get_correct_names()
    ya = Yandex(input('Введите токен с Полигона Яндекс.Диска.: '))
    ya.create_folder()
    ya.upload_from_internet()
