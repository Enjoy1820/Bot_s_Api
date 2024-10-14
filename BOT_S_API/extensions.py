import requests
import json

from config import keys

class APIExeption(Exception):
    pass

class Convertation:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIExeption("Валюты для сравнения одинаковые")

        try:
            quote_ticket = keys[quote]
        except KeyError:
            raise APIExeption(f"Валюта {quote} не может быть переведена" )

        try:
            base_ticket = keys[base]
        except KeyError:
            raise APIExeption(f"В Валюту {base} невозможно сконвертировать")

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIExeption(f"Последним введите число")

        r = requests.get(f"https://api.fastforex.io/fetch-one?from={quote_ticket}&to={base_ticket}&api_key=6a69a148cd-560a09c77f-sld34h")
        total_base = round(json.loads(r.content)["result"][base_ticket], 5) * amount

        return total_base