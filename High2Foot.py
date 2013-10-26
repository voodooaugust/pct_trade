from pandas import *

def getFile(code):
    url = 'http://ichart.finance.yahoo.com/table.csv?s=%s.HK&g=d&a=9&b=12&c=2010&ignore=.csv' % code
    df = read_csv(url,thousands=',',parse_dates=1)
    df = df.set_index('Date')
    df.index = to_datetime(df.index)
    price = df.ix[:df.High.argmax(),:5]
    price['foot'] = price.Close - price.Low
    return price
def setpricelist(ls):
    l = []
    for idx, each in ls.iteritems()
        l.append((idx,getFile(each)))
    return l
