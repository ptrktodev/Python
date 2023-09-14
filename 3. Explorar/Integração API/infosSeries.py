import requests

api_key = '04105f3a63399900b37fa84e3ec7168e'
urlApi = 'https://api.themoviedb.org/3/tv/popular'

params = {'api_key': api_key, 'page': 5}

re = requests.get(urlApi, params)

if re.status_code == 200:
    data = re.json()['results']
    listTv = [item for item in data if 'Chicago Fire' in item['name']]

print(f"A série {listTv[0]['name']} tem {listTv[0]['vote_average']} de pontuação, com um total de {listTv[0]['vote_count']} votos.")
            
       
        
        
         

