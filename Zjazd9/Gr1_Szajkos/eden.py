"""
Program który tłumaczy podany tekst z danego języka na polski.
"""
import click
import httpx
import keyring


@click.group()
def cli():
    ...


@cli.command
@click.argument("text")
@click.option("-sl", "--source-language", default="en")
@click.option("-tl", "--target-language", default="pl")
def translate(text: str, source_language: str = "en", target_language: str = "pl") -> str:
    print(source_language)
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
    result = response.json()["microsoft"]["text"]
    print(result)
    return result


@cli.command
@click.argument("api_key")
def login(api_key: str):
    keyring.set_password("eden", "api_key", api_key)
    print("API KEY set")


if __name__ == '__main__':
    cli()
