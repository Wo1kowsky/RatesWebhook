import pycbrf
import datetime
import json

def get_rate(params):
    type_of_currency = params.get("currency")
    today_date = datetime.date.today()
    return {'rate' : str(pycbrf.ExchangeRates(today_date)[type_of_currency].rate)}
