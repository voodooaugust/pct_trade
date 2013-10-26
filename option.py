# coding: utf-8
get_ipython().magic(u'cd E:\\Users\\august\\Documents\\google\\pct_trade/')
get_ipython().magic(u'run quant.py')
dir
import buildDataFrame as bdf
import buildDataFrame as bdf
bdf.build()
bdf.buildDataFrame().build()
import buildDataFrame as bdf
bdf.buildDataFrame().build()
import buildDataFrame
a = buildDataFrame()
import buildDataFrame as bdf
bdf.buildDataFrame().build()
import buildDataFrame
get_ipython().magic(u'run quant.py')
result = read_csv('trade_result.csv')
result
result = read_csv('trade_result.csv',index=0)
result = read_csv('trade_result.csv',index_col=[0,1])
result
result.where(result[-2] > result[-1])
result.where(result.icol(-2) > result.icol(-1))
result.icol(-1)
result.icol(-2)
result[result.icol(-2) > result.icol(-1)]
bf = result[result.icol(-2) > result.icol(-1)]
bf.index
DateOffset(days=-50,freq='B')
DateOffset(Bday=-20)
DateOffset(days=-2)
DateOffset(days=-20)
DateOffset(days=-20,freq='BDay')
6 * BDay()
from pandas.tseries.offsets import *
BDay()
today()
Date.today()
date.today()
from datetime import date
date.today()
date.today() - 50*BDay()
datetime.today()
datetime.today() - 50*BDay()
d = datetime.today() - 50*BDay()
d.day()
d.day
d.month
_.day
for code, mv in bf.index:
    para = code, str(d.day), str(d.month), str(d.year)
    url ='http://ichart.finance.yahoo.com/table.csv?s=%s.HK&g=d&a=%s&b=%s&c=%s&ignore=.csv' % para
    temp = read_csv(url,thousands=',',parse_dates=1,index_col=1)
    temp.index = to_datetime(temp.index)
    temp.to_csv('yahoodata/'+code+'.csv')
code = 777
para = str(code).zfill(4), d.day, d.month, d.year
para
url
url = 'http://ichart.finance.yahoo.com/table.csv?s=%s.HK&g=d&a=%s&b=%s&c=%s&ignore=.csv' % para
url
read_csv(url,index_col=1)
read_csv(url,index_col=[1])
read_csv(url,index_col=0)
import zipfile
def readzip():
    files = os.listdir('index_FO/')
    for each in files:
        a = ZipFile(each,'r')
        print ZipFile.namelist()
readzip()
def readzip():
    files = os.listdir('index_FO/')
    for each in files:
        a = zipfile.ZipFile(each,'r')
        print a.namelist()
readzip()
zipfile.ZipFile('index_FO/DTOP_F_20130927.zip','r')
a = zipfile.ZipFile('index_FO/DTOP_F_20130927.zip','r')
a.namelist()
ZipFile('index_FO/DTOP_F_20130927.zip','r')
a.infolist()
a.getinfo()
for each in a.namelist():
    a.read(each)
    a.close()
for each in a.namelist():
    f = a.open(each,'r')
    f.read()
    f.close()
a
for each in a.namelist():
    print a.read()
    
for each in a.namelist():
    print a.read(each)
a = zipfile.ZipFile('index_FO/DTOP_F_20130927.zip')
for each in a.namelist()
for each in a.namelist():
    print a.read(each)
    
a.namelist()
ls = a.namelist()
lambda x: if 'opt' and 'all.raw' in ls
lambda x: x if 'opt' and 'all.raw' in ls
(lambda x: x if 'opt' and 'all.raw' in x)(ls)
[x if 'opt' and 'all.raw' in ls]
[x for x in ls if 'opt' in x]
[x for x in ls if 'opt' and 'all.raw' in x]
[x for x in ls if 'opt' in x and 'all.raw' in x]
[x for x in ls if ('opt' and 'all.raw') in x]
x for x in ls if 'opt' in x
x for x in ls if 'opt' in xls
ls
ls = Series(ls)
ls
ls[17]
a.read(ls[17])
print a.read(ls[17])
print a.read(ls[24])
ls
print a.read(ls[25])
print a.read(ls[17])
DataFrame(a.read(ls[17]))
read_csv(a.read(ls[17]),sep=',')
b = read_csv(a.read(ls[17]),sep=',')
b
a.write('option.csv')
a.write('option.csv','w')
data = a.read(ls[17])
(lambda f, d: (f.write(d), f.close()))(open('opt.csv','w'),data)
read_csv('opt.csv',sep=',')
data
import re
pattern = '("01".*)\r\n"
pattern = '("01".*)\r\n'
re.findall(pattern, data)
t01 = re.findall(pattern, data)
DataFrame(t01)
[x.split(',') for x in t01]
t = [x.split(',') for x in t01]
DataFrame(t)
df = DataFrame(t)
df[10]
df[:2]
df[1]
df.irow(2)
colname = ['RecordType','Market','Marketname','Underlying','ExMonth','ExYear','strike','CALL_gross','CALL_net','CALL_netchange','CALL_TO','CALL_deal','CALL_settleprice','CALL_pricechange','PUT_gross','PUT_net','PUT_netchange','PUT_TO','PUT_deal','PUT_settleprice','PUT_pricechange']
df.columns = colname
df
df.set_index('RecordType','Market','Marketname','Underlying')
df = df.set_index('RecordType','Market','Marketname','Underlying')
df = df.set_index(['RecordType','Market','Marketname','Underlying'])
df
df
df = df.set_index(['Market','Marketname','Underlying'])
df
df[1]
df[2]
df.irow(2)
df.reset_index()
df
get_ipython().magic(u'save option.py _ih')
_ih[:}
get_ipython().magic(u'hist')
_ih
get_ipython().magic(u'save option.py _ih')
get_ipython().magic(u'save option.py _ih[:]')
get_ipython().magic(u'save option.py %hist')
_oh
_ih
get_ipython().magic(u'save option.py _ih')
get_ipython().magic(u'hist')
_ih[:]
get_ipython().magic(u'save option.py _ih')
get_ipython().magic(u'save option.py _ih[:]')
get_ipython().magic(u'save option.py')
get_ipython().magic(u'save option.py %history')
get_ipython().magic(u'store')
get_ipython().magic(u'pinfo %save')
get_ipython().magic(u'history [:]')
get_ipython().magic(u'history [4]')
get_ipython().magic(u'save option _ih[:]')
get_ipython().magic(u'save option.py In')
get_ipython().magic(u'save option.py In[:]')
In
get_ipython().magic(u'save option.py 1:')
_ih
get_ipython().magic(u'hist')
_ih[5]
_ih[:]
l = _ih[:]
get_ipython().magic(u'save option l')
get_ipython().magic(u'pinfo %save')
get_ipython().magic(u'pinfo %pastebin')
_ih
Series(_ih)
len(ih)
len(_ih)
get_ipython().magic(u'save option.py 1-183')
