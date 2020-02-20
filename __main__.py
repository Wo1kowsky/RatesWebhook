import pycbrf
import datetime
import json

def get_rate(params):
    today_date = datetime.date.today()
    return json.dumps({'rate' : str(pycbrf.ExchangeRates(today_date)['USD'].rate)})
