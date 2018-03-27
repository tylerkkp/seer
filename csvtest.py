import csv
import urllib.request
import json
import time
from random import *
import sqlite3
import pickle

statlist = ['symbol', 'companyName', 'primaryExchange', 'sector', 'calculationPrice',
    'open', 'openTime', 'close', 'closeTime', 'high', 'low', 'latestPrice', 'latestSource',
    'latestTime', 'latestUpdate', 'latestVolume', 'iexRealtimePrice',
    'iexRealtimeSize', 'iexLastUpdated', 'delayedPrice', 'delayedPriceTime', 'previousClose',
    'change', 'changePercent', 'iexMarketPercent', 'iexVolume', 'avgTotalVolume',
    'iexBidPrice', 'iexBidSize', 'iexAskPrice', 'iexAskSize', 'marketCap', 'peRatio',
    'week52High', 'week52Low', 'ytdChange']

#class stock:
    #def __init__(self):
        #self.data = []

#conn = sqlite3.connect('data.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE stocks
#             (symbol, companyName, primaryExchange, sector, calculationPrice,
#    open, openTime, close, closeTime, high, low, latestPrice, latestSource,
#    latestTime, latestUpdate, latestVolume, iexRealtimePrice,
#    iexRealtimeSize, iexLastUpdated, delayedPrice, delayedPriceTime, previousClose,
#    change, changePercent, iexMarketPercent, iexVolume, avgTotalVolume,
#    iexBidPrice, iexBidSize, iexAskPrice, iexAskSize, marketCap, peRatio,
#    week52High, week52Low, ytdChange)''')

def updatedata():
    symbol = dictwords.get('symbol')
    companyName = dictwords.get('companyName')
    primaryExchange = dictwords.get('primaryExchange')
    sector = dictwords.get('sector')
    calculationPrice = dictwords.get('calculationPrice')
    openPrice = dictwords.get('open')
    openTime = dictwords.get('openTime')
    close = dictwords.get('close')
    closeTime = dictwords.get('closeTime')
    high = dictwords.get('high')
    low = dictwords.get('low')
    latestPrice = dictwords.get('latestPrice')
    latestSource = dictwords.get('latestSource')
    #IEXrealtimeprice = dictwords.get('IEX real time price')
    latestTime = dictwords.get('latestTime')
    latestUpdate = dictwords.get('latestUpdate')
    latestVolume = dictwords.get('latestVolume')
    iexRealtimePrice = dictwords.get('iexRealtimePrice')
    iexRealtimeSize = dictwords.get('iexRealtimeSize')
    iexLastUpdated = dictwords.get('iexLastUpdated')
    delayedPrice = dictwords.get('delayedPrice')
    delayedPriceTime = dictwords.get('delayedPriceTime')
    previousClose = dictwords.get('previousClose')
    change = dictwords.get('change')
    changePercent = dictwords.get('changePercent')
    iexMarketPercent = dictwords.get('iexMarketPercent')
    iexVolume = dictwords.get('iexVolume')
    avgTotalVolume = dictwords.get('avgTotalVolume')
    iexBidPrice = dictwords.get('iexBidPrice')
    iexBidSize = dictwords.get('iexBidSize')
    iexAskPrice = dictwords.get('iexAskPrice')
    iexAskSize = dictwords.get('iexAskSize')
    marketCap = dictwords.get('marketCap')
    peRatio = dictwords.get('peRatio')
    week52High = dictwords.get('week52High')
    week52Low = dictwords.get('week52Low')
    ytdChange = dictwords.get('ytdChange')

with open ('ticklist.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    stockdict = {}
    for row in reader:
        tickername = row[0]
        url = 'https://api.iextrading.com/1.0/stock/'+tickername+'/quote'
        try:
            jsondata = urllib.request.urlopen(url)
            words =  jsondata.readlines()
            #unpack list 'words'
            wordsstr = words[0]
            #decode bytes value 'wordsstr' into string
            worddecoded = wordsstr.decode('utf-8')
            #convert string 'worddecoded' to a dictionary
            dictwords = json.loads(worddecoded)

            ticker = {}
            locals()[tickername] = ticker
            # Runs function to update all parameters
            #updatedata()
            for item in statlist:
               ticker[item] = dictwords.get(item)
               print(ticker[item])


            
            #print(type(dictwords))
            #print(dictwords)

###Insert a row of data
#c.execute("INSERT INTO stocks VALUES (symbol, companyName, primaryExchange, sector, calculationPrice, openPrice, openTime, close, closeTime, high, low, latestPrice, latestSource, latestTime, latestUpdate, latestVolume, iexRealtimePrice, iexRealtimeSize, iexLastUpdated, delayedPrice, delayedPriceTime, previousClose, change, changePercent, iexMarketPercent, iexVolume, avgTotalVolume, iexBidPrice, iexBidSize, iexAskPrice, iexAskSize, marketCap, peRatio, week52High, week52Low, ytdChange)")
###Save (commit) the changes
#conn.commit()
            #get value of specific key
            #close = dictwords.get('close')
            #print(close)
        except:
            print('there was an error')
            pass
        #sleep for 0.1-0.5 seconds, to limit excessive API calls
        time.sleep(randint(1,5)/10)

        stockdict[tickername] = ticker
        #break to pause process; for testing purposes only
        #x = input('press any key to continue')

    # Store data (serialize)
    with open('stockdata.pickle', 'wb') as handle:
        pickle.dump(stockdict, handle, protocol=pickle.HIGHEST_PROTOCOL)




        with open('stockdata.pickle', 'rb') as handle:
            content = pickle.load(handle)
        #print(list(content.keys()))

#close connection to the db
#conn.close()
            



##        url = 'https://api.iextrading.com/1.0/stock/'+ticker+'/quote'
##        r = requests.get(url)
##        print(r.json())


