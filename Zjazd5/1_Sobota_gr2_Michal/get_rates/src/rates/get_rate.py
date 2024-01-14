import click
import httpx


def get_rate(currency: str, internet=httpx):
    response = internet.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/last")
    rate_dict = response.json()["rates"][0]
    return rate_dict["mid"]


@click.command()
@click.argument("currency")
def main(currency: str):
    print(f"Kurs: {get_rate(currency)} PLN")
