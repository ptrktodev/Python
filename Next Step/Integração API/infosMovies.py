import requests

api_key = '04105f3a63399900b37fa84e3ec7168e'
urlApi = 'https://api.themoviedb.org/3/movie/popular'

params = {'api_key': api_key, 'page': 2}

re = requests.get(urlApi, params)

if re.status_code == 200:
    data = re.json()['results']
    title = [x['title'] for x in data]

print(title)




