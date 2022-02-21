import requests
import json

class CurrencyApi():
    def __init__(self, currency):
        self.currency = currency

    def callCurrencyBuying(self):
        api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/try/{self.currency}.json"

        result = requests.get(api_url)
        result = json.loads(result.text)

        return result[self.currency]

    def callCurrencySelling(self):
        api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{self.currency}/try.json"

        result = requests.get(api_url)
        result = json.loads(result.text)

        return result["try"]
