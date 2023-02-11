import requests
from pprint import pprint
from settings import vk_token


class VKontakte:
    """
    1)Получение информации о пользователе в ВК
    2)Получение списка фотографий
    3)Создание словаря (URL фотографии: количество лайков)
    """

    dict_of_photos = {}
    list_of_likes = []
    list_of_dates = []

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
             f"{dict_of_photo_info['response']['items'][i]['likes']['count']}"
        pprint("Фотографии получены")
        pprint(self.dict_of_photos)
        #self.list_of_likes.append(0)
        #self.list_of_likes.reverse()
        pprint(self.list_of_likes)

    def get_correct_names(self):
        for a in self.dict_of_photos:
            for b in range(len(self.list_of_likes)):
                if int(self.dict_of_photos[a]) == self.list_of_likes[b]:




class Yandex(VKontakte):

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
        response = requests.put(f'{request_url}?path={path}', headers=self.get_headers())
        pprint("Папка создана")
        return

    def upload_from_internet(self):
        for url in VKontakte.dict_of_photos:
            uri = 'v1/disk/resources/upload/'
            request_url = self.base_host + uri
            yandex_path = '/' + f'{self.folder_name}/' + VKontakte.dict_of_photos[url] + '.jpg'
            params = {'url': url, 'path': yandex_path}
            response = requests.post(request_url, params=params, headers=self.get_headers())
            pprint('Фотография добавлена')


if __name__ == '__main__':
    vk = VKontakte(vk_token)
    vk.get_profile_photos()
    vk.get_correct_names()
    #ya = Yandex(input('Введите токен с Полигона Яндекс.Диска.: '))
    #ya.create_folder()
    #ya.upload_from_internet()
