import requests
from pprint import pprint
base_host = 'https://cloud-api.yandex.net/'
uri = '/v1/disk/resources'
request_url = base_host +uri
params = {'url': request_url, 'path': '/'}
headers = {
'Content-Type': 'application/json',
'Authorization': f'OAuth y0_AgAAAABnidfKAADLWwAAAADa_z78ZjqH_4g7QducxQa5eUB00MWCLaA'
}

pprint()