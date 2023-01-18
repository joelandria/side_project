import requests


def get_json(url):
    response = requests.get(url)

    json = response.json()

    response.close()
    return json
