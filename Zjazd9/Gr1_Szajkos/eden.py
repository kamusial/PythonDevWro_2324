"""
Program który tłumaczy podany tekst z danego języka na polski.
"""
import httpx
import keyring


def translate(text: str, source_language: str = "en", target_language: str = "pl") -> str:
    api_key = keyring.get_password("eden", "api_key")
    url = "https://api.edenai.run/v2/translation/automatic_translation"
    payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_original_response": False,
        "providers": "microsoft",
        "text": text,
        "source_language": source_language,
        "target_language": target_language
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    response = httpx.post(url, json=payload, headers=headers)
    return response.json()["microsoft"]["text"]


def login(api_key: str):
    keyring.set_password("eden", "api_key", api_key)


print(translate("I love pancakes"))
