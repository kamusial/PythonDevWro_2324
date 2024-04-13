import httpx
import json


def get_today_eur_rate():
    url = "https://api.nbp.pl/api/exchangerates/rates/a/eur/last"
    response = httpx.get(url)
    print(response.json())


def get_eden_list_providers_subfeatures():
    url = "https://api.edenai.run/v2/info/provider_subfeatures"
    headers = {"accept": "application/json"}
    response = httpx.get(url, headers=headers)
    print(json.dumps(response.json(), indent=4))


if __name__ == '__main__':
    get_eden_list_providers_subfeatures()
