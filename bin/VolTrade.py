# Hello World program in Python
    
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import urllib
import tempfile as tp
import os
import sys
import requests
from datetime import datetime
import time
        
def downloadfile(stock, f = 'sd1t1vml1c1p2k4k5a2'):
  
    baseurl = 'http://finance.yahoo.com/d/quotes.csv?%s'
    stock = ['{:0>4}'.format(x) + '.HK' for x in stock]
    s = '+'.join(stock)
  
    paras = urllib.urlencode({'s': s, 'f': f})
    f = urllib.urlopen(baseurl % paras)
     
    # sd1t1vml1c1p2k4k5a2
    colname = ['symbol', 'date', 'time', 'volume', 
               'daily_rng', 'last_price', 
               'change', 'change_pct', '52wH', '52wH_pct', 'avg_vol']
    data = pd.read_csv(f, names=colname)  
    data = data.set_index(['symbol']) 
    
    f.close()
    print data
    return data 
    # construct multiIndex
    
def getRecord(stock, period=10):
    if period == None:
        period = 10 
    else:
        period = int(period)
    home = os.path.dirname(os.getcwd())
    filename = '{:%Y%m%d-%H%M}'.format(datetime.today()) 

    # dirname = '{:0>4}'.format(stock)
    # for x in stock:
    #     directory = os.join.path(home, x)
    #     if not os.path.exists(directory):
    #         os.makedirs(directory)
    dest = os.path.join(home, 'data', filename)
            
    for x in range(period): 
        data = downloadfile(stock)
        data.to_csv(dest)
        time.sleep(180)
    # store data
def quote():
    home = os.path.dirname(os.getcwd())
    datahome = os.path.join(home, 'data','')
        
        # timestr = datetime.strftime(datetime.now(), '%D%H%M')
        # data.to_csv(os.path.join(datahome, timestr + '.csv'), index=False)
        
    def getStocklist():
        home = os.path.dirname(os.getcwd())
        ls = os.path.join(home, 'data', 'stock_list.xls')
        ls = pd.read_excel(ls)
        return ls
    def a2():
        ls = getStocklist()
        downloadfile(ls[0])
        
        
    ls = getStocklist()
    # code = ['1398', '939', '1']
    d = pd.DataFrame()



    # can be set to time end at 1600
    # store data to data directory
    now = datetime.now()
    count = 0
    while not ((now.hour > 15) and (now.minute >20)):
        d = pd.DataFrame()
        for x in range(0, len(ls), 100):
            code = ls['STOCK CODE'][x:x+100]
            data = downloadfile(code)
        #     print data
            d = d.append(data)
            d = d[d['volume'] > 0]
            print d
        d.to_csv(datahome + '{:0>2}.csv'.format(count))    
        now = datetime.now()
        print 'current time {}'.format (now)
        count += 1
        time.sleep(180)
    # codeset = list(ls['STOCK CODE'][1500:])
    # downloadfile(codeset)



def histDownload(code):
    code = '{:0>4}.hk'.format(code)
    home = os.path.dirname(os.getcwd())
    datadir = os.path.join(home, 'data', code + '.csv')
    def datetime_timestamp(dt):
         time.strptime(dt, '%Y-%m-%d %H:%M:%S')
         s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
         return str(int(s))

    s = requests.Session()

    #Replace B=xxxx
    cookies = dict(B='c650m5hchrhii&b=3&s=tk')

    #Replace crumb=yyyy
    crumb = 'NMhMTCv7QpM'

    begin = datetime_timestamp("2014-01-01 09:00:00")

    end =  str(int(time.time()))
    
    r = s.get("https://query1.finance.yahoo.com/v7/finance/download/%s?period1=" % code
              +begin+"&period2="+end+"&interval=1d&events=history&crumb="+crumb,cookies=cookies,verify=False)
    
    f = open(datadir, 'w')
    f.write(r.text)
    f.close()

def getStocklist():
    home = os.path.dirname(os.getcwd())
    ls = os.path.join(home, 'data', 'stock_list.xls')
    ls = pd.read_excel(ls)
    return ls

# d = {}
# ls = getStocklist()[0]
# for code in ls['STOCK CODE']:
#     print 'downloading %s \n' % code
#     d['{:0>4}'.format(code)] = histDownload(code)


if __name__ == '__main__':
    if len(sys.argv) == 2 :
        sys.exit()
        print len(sys.argv)
    elif len(sys.argv) == 1:
        print 'programme started'
        quote()

    print len(sys.argv)
    arg = sys.argv
    # histDownload(939)


    print 'all is done'
