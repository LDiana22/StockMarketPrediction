# Predicting the predictable causes the predictable to become unpredictable

import requests

url = "https://rapidapi.p.rapidapi.com/query"

querystring = {"function":"GLOBAL_QUOTE","symbol":"DAL"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "5380afb53dmsh7f5757bdb168201p180fcejsn8e72f10a22cd"
    }

stoncks = ["DAL", "SPXL", "AC", "ONTX"]

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

querystring = {"function":"TIME_SERIES_DAILY_ADJUSTED", "symbol":"DAL", "outputsize":"compact"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)