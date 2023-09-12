import requests

api_key = '04105f3a63399900b37fa84e3ec7168e'
ids = []
url = 'https://api.themoviedb.org/3/movie/popular'

for pages in range(0, 3):

    params = {'api_key': api_key, 'page': pages}

    resposta1 = requests.get(url, params, timeout=4)
    if resposta1.status_code == 200:
        print("Solicitação foi bem-sucedida.")
        data = resposta1.json()
        print(f"Filmes da Página {data['page']}:")
        if "results" in data:
            for x in data['results']:
                ids.append(x['id'])
    else:
        status_code = resposta1.status_code
        if status_code == 401:
            print('Credenciais fornecidas são inválidas ou ausentes.')
        elif status_code == 400:
            print("Solicitação está mal formada ou contém parâmetros inválidos.")
        elif status_code == 404:
            print("Recurso solicitado não foi encontrado no servidor")

    for numbers_ID in ids:
        resposta2 = requests.get(f"https://api.themoviedb.org/3/movie/{numbers_ID}", params=params)
        if resposta2.status_code == 200:
            data = resposta2.json()
            print(data['original_title'])
        else:
            print(f"codigo de status: {resposta2.status_code}")