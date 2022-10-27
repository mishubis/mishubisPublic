import requests
import json
from config import keys

class ConversionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}&api_key=d8c9b0021329f443295dc65c56ffa14fec947dc00cfa0a8fab8e27e113e68367')
        total_base = json.loads(r.content)[keys[base]]
        total_base = amount * total_base
        return total_base
