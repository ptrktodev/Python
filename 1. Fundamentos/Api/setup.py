import requests

for number in range(1, 5):

    key = "04105f3a63399900b37fa84e3ec7168e";
    url = f"https://api.themoviedb.org/3/tv/popular?api_key={key}&langauge=en-US&page={number}";
    api = requests.get(url)

    if api.status_code == 200:
        data = api.json()
        results = data['results']
        for i in range(0, len(results)):
            print(results[i]['original_name'])
    else:
        pass

