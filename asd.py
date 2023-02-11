import requests
from pprint import pprint

url = "https://api.vk.com/method/photos.get"
params = {
'access_token': 'vk1.a.GrxGsV8OF3UzGmwA8WyaJtJuDMjnTElDYE1XZhHEJq-qwunlnn87s7ialxPlbaCuXfsFbA8PgoqpJpbg47ZmuPellByesJtW4ze9llP6Ta4pBqxW0BptlWPR7AtcHMaNwX9cEoyYoxfoQxnuaPZUcdtD7noWlC1ZJw9Fx0HKoSeMZCfGMjaf53W8NmxXWwHP2cYHkLe0LLZJFYG8AjJsdA',
            'owner_id': '213358442',
            'album_id': 'profile',
            'v': '5.131'}
res = requests.get(url, params=params)
pprint(res.json())
