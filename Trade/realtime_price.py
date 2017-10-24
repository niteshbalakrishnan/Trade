import urllib.request

import json


def google(ticker):

    url = 'http://finance.google.com/finance/info?client=ig&q=NSE%3ABHEL'

    doc = urllib.request.urlopen(url)

    content = doc.read()

    quote = json.loads(content[3:])

    quote = float(quote[0][u'l'])

    return quote



if __name__ == "__main__":

    ticker = 'NSE'
    x= google(ticker)
    print(x)