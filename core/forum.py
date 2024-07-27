import requests

def get_threads(url, token):
    headers = {
        "accept": "application/json",
        "authorization": "Bearer {}".format(token)
    }

    response = requests.get(url, headers=headers)
    return response.json()