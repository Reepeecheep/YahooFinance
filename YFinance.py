import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_SECRET_KEY = str(os.getenv('API_SECRET_KEY'))

NAMES = {
    "^N225": "Nikkei 225",
    "^DAX-EU": "DAX Index", 
    "^IXIC": "Nasdaq",
}

url = "https://yfapi.net/v6/finance/quote/"

headers = {
    'x-api-key': API_SECRET_KEY
}

querystring = {"symbols":"^N225,^DAX-EU,^IXIC,AAPL,AMZN,FB,GOOG"}

def getFinanceData():
    data = {}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.json()['quoteResponse']['result']

        if response.status_code == 200 and result != []:
            for r in result:
                data[r['symbol']] = float(r['regularMarketPrice'])
        return data
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)