# IPython log file

get_ipython().magic(u'cd E:\\Users\\august\\Documents\\google\\pct_trade/')
get_ipython().magic(u'run quant.py')
dir
import buildDataFrame as bdf
import buildDataFrame as bdf
import buildDataFrame as bdf
import buildDataFrame as bdf
import buildDataFrame as bdf
import buildDataFrame as bdf
import buildDataFrame as bdf
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
get_ipython().magic(u'pwd')
df
df.CALL_net
df['HSI']
df.row('HSI')
df
df.row('XHS')
df.index
set(df.index)
df = df.reset_index()
df
del df.Market df.Marketname
del df.Market
del df[['Market','Marketname',]]
df
del df['Market']
df
del df['Marketname']
df
df.ExMonth
df.ExYear
df
df.ExMonth + df.ExYear
df.ExMonth.join(df.ExYear)
df['ExMonth'].join(df.ExYear)
df['ExMonth'].apply(join(df.ExYear))
df['ExMonth'].apply(''.join(df.ExYear))
to_datetime([df.ExMonth,df.ExYear])
df
df.index
df
ndf = df.set_index(['Underlying','ExMonth','ExYear','strike'])
ndf
ndf.reset_index()
df
ndf
df
del ndf
dir()
get_ipython().magic(u'logstart')
get_ipython().magic(u'pwd')
df
df.['ttm'] = df.ExMonth +'-'+ df.ExYear
df['ttm'] = df.ExMonth +'-'+ df.ExYear
df
df.ttm
df.ttm.strip('"')
df.ttm.apply(strip('"'))
df.ttm.apply(lambda x : x.strip('"'))
df.ttm.apply(lambda x : x.strip('"''))
df.ttm.apply(lambda x : x.strip('"'''))
df.ExYear.apply(lambda x : x.strip('"'))
df.ExMonth.apply(lambda x : x.strip('"'))
df.ttm
df.ttm.apply(lambda x:x.strip("'"))
df.ttm.apply(lambda x:x.strip("''"))
df.ttm.apply(lambda x:x.strip('\"'))
df.ttm.apply(lambda x:x.replace('"',''))
df.ttm = df.ttm.apply(lambda x:x.replace('"',''))
to_datetime(df.ttm)
to_datetime(df.ttm,format='%b-%y')
to_datetime(df.ttm,format='%b-%y',freq='EOM')
to_datetime(df.ttm,format='%b-%y')
df.ttm = to_datetime(df.ttm,format='%b-%y')
df.ttm.asfreq(BDay())
df.ttm.asfreq('M')
df.ttm
df.ttm.apply(lambda x:x.strftime('%y%m'))
df.ttm.apply(lambda x:x.strftime('%y-%m'))
df.ttm.apply(lambda x:x.strftime('%y/%m'))
df.ttm = df.ttm.apply(lambda x:x.strftime('%y/%m'))
df.ttm
df.ttm
to_datetime(df.ttm,format='%y/%m)
to_datetime(df.ttm,format='%y/%m')
df.ttm.to_timestamp('M')
df.ttm.to_period()
PeriodIndex(df.ttm)
PeriodIndex(df.ttm,freq='M')
Period(df.ttm)
df.index = df.ttm
df.index
df.reset_index()
df.ttm
df.index
df.ttm
del df.ttm
del df['ttm']
df.reset_index()
df.ttm = to_datetime(df.ttm,format='%y/%m')
df
df.reset_index()
df = df.reset_index()
df.ttm = to_datetime(df.ttm, format='%y/%m')
df.ttm
df.set_index('ttm')
df = df.set_index('ttm')
df
del df[['ExMonth','ExYear']]
del df['ExMonth']
del df['ExYear']
df
df = df.reset_index()
df
df.set_index('Underlying')
df
df = df.set_index('Underlying')
df
DatetimeIndex(df.ttm,freq='D')
Period(df.ttm,freq='D')
df
df.ttm.convert('D',method='pad')
df
df.ttm.astype(datetime)
df['HSI']
df['XHS']
df.index = df.index.apply(lambda x: x.replace('"',''))
df.reset_index()
df = df.reset_index()
df.Underlying = df.Underlying.apply(lambda x: x.replace('"',''))
df = df.set_index('Underlying')
df
df['HSI']
df.index
df.row('HSI')
df.ix['HSI']
hsi = df.ix['HSI']
hsi
hsi = hsi.reset_index()
hsi
hsi = df.ix['HSI']
hsi.pivot(index='ttm',columns='strike',values=['CALL_net','PUT_net'])
hsi.pivot(index='ttm',columns='strike',values='CALL_net')
hsi.CAll_net
hsi
hsi['CALL_net']
hsi.pivot(index='ttm',columns='strike',values='CALL_net')
hsi.pivot(index='ttm',columns='strike',values='CALL_net',aggfunc=sum)
hsi.pivot(index='ttm',columns='strike',values='CALL_net')
pivot_table(hsi,values='CALL_net',rows='strike',cols='ttm')
hsi
hsi['CALL_net']
hsi['CALL_net'].asdtype(int)
hsi['CALL_net'].astype(int)
hsi.CALL_net = hsi['CALL_net'].astype(int)
hsi
hsi.apply(lambda x:x.astype(float))
hsi.ix[:,1:].apply(lambda x:x.astype(float))
hsi.ix[:,1:] = hsi.ix[:,1:].apply(lambda x:x.astype(float))
hsi
hsi
hsi.ix[:,1:].apply(lambda x:x.astype(float))
hsi.ix[:,1:]=hsi.ix[:,1:].apply(lambda x:x.astype(float))
hsi
hsi.ix[:,1:]=hsi.ix[:,1:].apply(lambda x:x.astype(float)).copy()
hsi
hsi.ix[:,1:].astype(float)
hsi
hsi.ix[:,1:] = hsi.ix[:,1:].astype(float)
hsi
hsi[1:]
hsi[[:]]
hsi[hsi.columns[1:]].astype(float)
hsi
hsi[hsi.columns[1:]]=hsi[hsi.columns[1:]].astype(float)
hsi
pt = pivot_table(hsi,values='CALL_net',rows='strike',cols='ttm')
pt.plot()
pt.plot(kind='dot')
pt
pt.plot(kind='bar')
pt.T.hist()
hsi
pt
pt.apply(count())
from matplotlib.colors import LinearSegmentedColormap
from pandas.tools.plotting import scatter_matrix
scatter_matrix(pt)
pt
pt[3]
pt.loc(2)
pt.iloc(2)
pt.iloc[2]
pt
pt.plot(kind='bar')
pt.plot(legend=0,kind='bar')
hsi
pivot_table(hsi,values=['CALL_net','PUT_net'],rows='strike',cols='ttm')
pt = pivot_table(hsi,values=['CALL_net','PUT_net'],rows='strike',cols='ttm')
pt.plot(legend=0,kind='bar')
z
pt['22200']
pt.loc['22200']
pt.index
pt.loc[22200.0]
 pt.index
pt.index
pt
get_ipython().magic(u'hsit')
get_ipython().magic(u'hist')
get_ipython().magic(u'load ipython_log.py')
hsi
datetime.today() - hsi.ttm
hsi.ttm - datetime.today()
hsi.groupby('ttm')
grouped = hsi.groupby('ttm')
grouped
for name, group in grouped:
    print name
    print group
    
for name, group in grouped:
    if 0 < name - datetime.today() < 60:
        print name
        print group
for name, group in grouped:
    if 0 < int(name - datetime.today()) < 60:
        print name
        print group
for name, group in grouped:
    if 0 < (name - datetime.today()).days() < 60:
        print name
        print group
for name, group in grouped:
    if 0 < (name - datetime.today()).days < 60:
        print name
        print group
for name, group in grouped:
    if -10 < (name - datetime.today()).days < 60:
        print name
        print group
for name, group in grouped:
    if -10 < (name - datetime.today()).months < 3:
        print name
        print group
for name, group in grouped:
    if -10 < (name - datetime.today()).month < 3:
        print name
        print group
ls = []
for name, group in grouped:
    if -10 < (name - datetime.today()).days < 50:
        print name
        ls.append(group)
ls
ls[1]
ls[0]
(ls[0].CALL_net + ls[0].PUT_net).plot(legend=0,kind='bar')
(ls[0].CALL_net + ls[0].PUT_net).set_index('strike').plot(legend=0,kind='bar')
ls[0].set_index('strike')
print ls[0]

a = ls[0].set_index('strike')
(a.CALL_net*a.CALL_settleprice - a.PUT_net * a.PUT_settleprice).plot(legend=0,kind='bar')



val = a.CALL_net*a.CALL_settleprice - a.PUT_net * a.PUT_settleprice
val
val.where(val >1000)
val.where(val >1000).dropna()
val.where(abs(val) >1000).dropna()
val.where(abs(val) >1000).dropna().plot(legend=0,kind='bar')
ls[0]
ls[0].idxmax()
ls[0].iloc[2:].idxmax()
ls[0]
ls[0].iloc[2:]
ls[0].ix[:,2:]
ls[0].ix[:,2:].idxmax()
a
slice(1,2)
a
a.ix[:,1:].idxmax()
a
a.ttm
hsi
hsi = hsi.set_index('strike')
hsi
for mat, group in hsi.groupby('ttm'):
    print mat
hsi.ttm = hsi.ttm.date()
hsi.ttm = hsi['ttm'].date()
hsi.ttm = hsi['ttm'].apply(lambda x: x.date())
hsi.ttm
from datetime import date
for t, group in hsi.groupby('ttm'):
    if t.month = date.today().month:
        print group
for t, group in hsi.groupby('ttm'):
    if t.month == date.today().month:
        print group
for t, group in hsi.groupby('ttm'):
    if t.month == date.today().month:
        with group as a:
            a['value'] = a.CALL_net * a.CALL_settleprice - a.PUT_net * a.PUT_settleprice - exp(0.102860)*a.index
            
for t, group in hsi.groupby('ttm'):
    if t.month == date.today().month:
        a = group
        a['value'] = a.CALL_net * a.CALL_settleprice - a.PUT_net * a.PUT_settleprice - exp(0.102860)*a.index
for t, group in hsi.groupby('ttm'):
    if t.month == date.today().month:
        a = group
        a['value'] = a.CALL_net * a.CALL_settleprice - a.PUT_net * a.PUT_settleprice - exp(0.102860)*a.index.astype(float)
for t, group in hsi.groupby('ttm'):
    if t.month == date.today().month:
        a = group
        a['value'] = a.CALL_net * a.CALL_settleprice - a.PUT_net * a.PUT_settleprice - exp(0.102860)*a.index.values
a
a.value.plot(kind='bar')
a[['CALL_net','PUT_net']].plot()
a[['CALL_net','PUT_net','value']].plot()
a
a[['CALL_net','PUT_net','value']].plot(kind='bar')
a['value'].plot()
a.idxmax()
a
a.ix[:,1:].idxmax()
a.value.type()
a.value.type
a['value'].type
a['value'].type()
type(a.value)
a.dtype
a.dtype()
a.value.dtype()
a.value.dtype
a['value'] = a.CALL_net * a.CALL_settleprice - a.PUT_net * a.PUT_settleprice - exp(0.102860)*a.index.values
a.value.dtype
a.value
a['value'].astype(float)
a.value
a['value']=a['value'].astype(float)
a.ix[:,1:].idxmax()
type(slice(1,2))
a[2]
a[[1,2]]
a[slice(1,2)]
a[[slice(1,2)]]
a.index.value
a.index.values
a.index.values.astype(float)
get_ipython().magic(u'logstate')
get_ipython().magic(u'logstop')
get_ipython().magic(u'cd E:\\Users\\august\\Documents\\google\\pct_trade/')
get_ipython().magic(u'run quant.py')
dir
import buildDataFrame as bdf
import buildDataFrame as bdf
import buildDataFrame as bdf
import buildDataFrame as bdf
import buildDataFrame as bdf
import buildDataFrame as bdf
import buildDataFrame as bdf
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
get_ipython().magic(u'pwd')
df
df.CALL_net
df['HSI']
df.row('HSI')
df
df.row('XHS')
df.index
set(df.index)
df = df.reset_index()
df
del df.Market df.Marketname
del df.Market
del df[['Market','Marketname',]]
df
del df['Market']
df
del df['Marketname']
df
df.ExMonth
df.ExYear
df
df.ExMonth + df.ExYear
df.ExMonth.join(df.ExYear)
df['ExMonth'].join(df.ExYear)
df['ExMonth'].apply(join(df.ExYear))
df['ExMonth'].apply(''.join(df.ExYear))
to_datetime([df.ExMonth,df.ExYear])
df
df.index
df
ndf = df.set_index(['Underlying','ExMonth','ExYear','strike'])
ndf
ndf.reset_index()
df
ndf
df
del ndf
dir()
get_ipython().magic(u'logstart')
get_ipython().magic(u'pwd')
df
df.['ttm'] = df.ExMonth +'-'+ df.ExYear
df['ttm'] = df.ExMonth +'-'+ df.ExYear
df
df.ttm
df.ttm.strip('"')
df.ttm.apply(strip('"'))
df.ttm.apply(lambda x : x.strip('"'))
df.ttm.apply(lambda x : x.strip('"''))
df.ttm.apply(lambda x : x.strip('"'''))
df.ExYear.apply(lambda x : x.strip('"'))
df.ExMonth.apply(lambda x : x.strip('"'))
df.ttm
df.ttm.apply(lambda x:x.strip("'"))
df.ttm.apply(lambda x:x.strip("''"))
df.ttm.apply(lambda x:x.strip('\"'))
df.ttm.apply(lambda x:x.replace('"',''))
df.ttm = df.ttm.apply(lambda x:x.replace('"',''))
to_datetime(df.ttm)
to_datetime(df.ttm,format='%b-%y')
to_datetime(df.ttm,format='%b-%y',freq='EOM')
to_datetime(df.ttm,format='%b-%y')
df.ttm = to_datetime(df.ttm,format='%b-%y')
df.ttm.asfreq(BDay())
df.ttm.asfreq('M')
df.ttm
df.ttm.apply(lambda x:x.strftime('%y%m'))
df.ttm.apply(lambda x:x.strftime('%y-%m'))
df.ttm.apply(lambda x:x.strftime('%y/%m'))
df.ttm = df.ttm.apply(lambda x:x.strftime('%y/%m'))
df.ttm
df.ttm
to_datetime(df.ttm,format='%y/%m)
to_datetime(df.ttm,format='%y/%m')
df.ttm.to_timestamp('M')
df.ttm.to_period()
PeriodIndex(df.ttm)
PeriodIndex(df.ttm,freq='M')
Period(df.ttm)
df.index = df.ttm
df.index
df.reset_index()
df.ttm
df.index
df.ttm
del df.ttm
del df['ttm']
df.reset_index()
df.ttm = to_datetime(df.ttm,format='%y/%m')
df
df.reset_index()
df = df.reset_index()
df.ttm = to_datetime(df.ttm, format='%y/%m')
df.ttm
df.set_index('ttm')
df = df.set_index('ttm')
df
del df[['ExMonth','ExYear']]
del df['ExMonth']
del df['ExYear']
df
df = df.reset_index()
df
df.set_index('Underlying')
df
df = df.set_index('Underlying')
df
DatetimeIndex(df.ttm,freq='D')
Period(df.ttm,freq='D')
df
df.ttm.convert('D',method='pad')
df
df.ttm.astype(datetime)
df['HSI']
df['XHS']
df.index = df.index.apply(lambda x: x.replace('"',''))
df.reset_index()
df = df.reset_index()
df.Underlying = df.Underlying.apply(lambda x: x.replace('"',''))
df = df.set_index('Underlying')
df
df['HSI']
df.index
df.row('HSI')
df.ix['HSI']
hsi = df.ix['HSI']
hsi
hsi = hsi.reset_index()
hsi
hsi = df.ix['HSI']
hsi.pivot(index='ttm',columns='strike',values=['CALL_net','PUT_net'])
hsi.pivot(index='ttm',columns='strike',values='CALL_net')
hsi.CAll_net
hsi
hsi['CALL_net']
hsi.pivot(index='ttm',columns='strike',values='CALL_net')
hsi.pivot(index='ttm',columns='strike',values='CALL_net',aggfunc=sum)
hsi.pivot(index='ttm',columns='strike',values='CALL_net')
pivot_table(hsi,values='CALL_net',rows='strike',cols='ttm')
hsi
hsi['CALL_net']
hsi['CALL_net'].asdtype(int)
hsi['CALL_net'].astype(int)
hsi.CALL_net = hsi['CALL_net'].astype(int)
hsi
hsi.apply(lambda x:x.astype(float))
hsi.ix[:,1:].apply(lambda x:x.astype(float))
hsi.ix[:,1:] = hsi.ix[:,1:].apply(lambda x:x.astype(float))
hsi
hsi
hsi.ix[:,1:].apply(lambda x:x.astype(float))
hsi.ix[:,1:]=hsi.ix[:,1:].apply(lambda x:x.astype(float))
hsi
hsi.ix[:,1:]=hsi.ix[:,1:].apply(lambda x:x.astype(float)).copy()
hsi
hsi.ix[:,1:].astype(float)
hsi
hsi.ix[:,1:] = hsi.ix[:,1:].astype(float)
hsi
hsi[1:]
hsi[[:]]
hsi[hsi.columns[1:]].astype(float)
hsi
hsi[hsi.columns[1:]]=hsi[hsi.columns[1:]].astype(float)
hsi
pt = pivot_table(hsi,values='CALL_net',rows='strike',cols='ttm')
pt.plot()
pt.plot(kind='dot')
pt
pt.plot(kind='bar')
pt.T.hist()
hsi
pt
pt.apply(count())
from matplotlib.colors import LinearSegmentedColormap
from pandas.tools.plotting import scatter_matrix
scatter_matrix(pt)
pt
pt[3]
pt.loc(2)
pt.iloc(2)
pt.iloc[2]
pt
pt.plot(kind='bar')
pt.plot(legend=0,kind='bar')
hsi
pivot_table(hsi,values=['CALL_net','PUT_net'],rows='strike',cols='ttm')
pt = pivot_table(hsi,values=['CALL_net','PUT_net'],rows='strike',cols='ttm')
pt.plot(legend=0,kind='bar')
z
pt['22200']
pt.loc['22200']
pt.index
pt.loc[22200.0]
 pt.index
pt.index
pt
get_ipython().magic(u'hsit')
get_ipython().magic(u'hist')
get_ipython().magic(u'load ipython_log.py')
hsi
datetime.today() - hsi.ttm
hsi.ttm - datetime.today()
hsi.groupby('ttm')
grouped = hsi.groupby('ttm')
grouped
for name, group in grouped:
    print name
    print group
    
for name, group in grouped:
    if 0 < name - datetime.today() < 60:
        print name
        print group
for name, group in grouped:
    if 0 < int(name - datetime.today()) < 60:
        print name
        print group
for name, group in grouped:
    if 0 < (name - datetime.today()).days() < 60:
        print name
        print group
for name, group in grouped:
    if 0 < (name - datetime.today()).days < 60:
        print name
        print group
for name, group in grouped:
    if -10 < (name - datetime.today()).days < 60:
        print name
        print group
for name, group in grouped:
    if -10 < (name - datetime.today()).months < 3:
        print name
        print group
for name, group in grouped:
    if -10 < (name - datetime.today()).month < 3:
        print name
        print group
ls = []
for name, group in grouped:
    if -10 < (name - datetime.today()).days < 50:
        print name
        ls.append(group)
ls
ls[1]
ls[0]
(ls[0].CALL_net + ls[0].PUT_net).plot(legend=0,kind='bar')
(ls[0].CALL_net + ls[0].PUT_net).set_index('strike').plot(legend=0,kind='bar')
ls[0].set_index('strike')
print ls[0]
a = ls[0].set_index('strike')
(a.CALL_net*a.CALL_settleprice - a.PUT_net * a.PUT_settleprice).plot(legend=0,kind='bar')
val = a.CALL_net*a.CALL_settleprice - a.PUT_net * a.PUT_settleprice
val
val.where(val >1000)
val.where(val >1000).dropna()
val.where(abs(val) >1000).dropna()
val.where(abs(val) >1000).dropna().plot(legend=0,kind='bar')
ls[0]
ls[0].idxmax()
ls[0].iloc[2:].idxmax()
ls[0]
ls[0].iloc[2:]
ls[0].ix[:,2:]
ls[0].ix[:,2:].idxmax()
a
slice(1,2)
a
a.ix[:,1:].idxmax()
a
a.ttm
hsi
hsi = hsi.set_index('strike')
hsi
for mat, group in hsi.groupby('ttm'):
    print mat
hsi.ttm = hsi.ttm.date()
hsi.ttm = hsi['ttm'].date()
hsi.ttm = hsi['ttm'].apply(lambda x: x.date())
hsi.ttm
from datetime import date
for t, group in hsi.groupby('ttm'):
    if t.month = date.today().month:
        print group
for t, group in hsi.groupby('ttm'):
    if t.month == date.today().month:
        print group
for t, group in hsi.groupby('ttm'):
    if t.month == date.today().month:
        with group as a:
            a['value'] = a.CALL_net * a.CALL_settleprice - a.PUT_net * a.PUT_settleprice - exp(0.102860)*a.index
            
for t, group in hsi.groupby('ttm'):
    if t.month == date.today().month:
        a = group
        a['value'] = a.CALL_net * a.CALL_settleprice - a.PUT_net * a.PUT_settleprice - exp(0.102860)*a.index
for t, group in hsi.groupby('ttm'):
    if t.month == date.today().month:
        a = group
        a['value'] = a.CALL_net * a.CALL_settleprice - a.PUT_net * a.PUT_settleprice - exp(0.102860)*a.index.astype(float)
for t, group in hsi.groupby('ttm'):
    if t.month == date.today().month:
        a = group
        a['value'] = a.CALL_net * a.CALL_settleprice - a.PUT_net * a.PUT_settleprice - exp(0.102860)*a.index.values
a
a.value.plot(kind='bar')
a[['CALL_net','PUT_net']].plot()
a[['CALL_net','PUT_net','value']].plot()
a
a[['CALL_net','PUT_net','value']].plot(kind='bar')
a['value'].plot()
a.idxmax()
a
a.ix[:,1:].idxmax()
a.value.type()
a.value.type
a['value'].type
a['value'].type()
type(a.value)
a.dtype
a.dtype()
a.value.dtype()
a.value.dtype
a['value'] = a.CALL_net * a.CALL_settleprice - a.PUT_net * a.PUT_settleprice - exp(0.102860)*a.index.values
a.value.dtype
a.value
a['value'].astype(float)
a.value
a['value']=a['value'].astype(float)
a.ix[:,1:].idxmax()
type(slice(1,2))
a[2]
a[[1,2]]
a[slice(1,2)]
a[[slice(1,2)]]
a.index.value
a.index.values
a.index.values.astype(float)
get_ipython().magic(u'logstate')
get_ipython().magic(u'logstop')
get_ipython().magic(u'logstart ipython_log.py append')
a
import urllib
a
a = zipfile.ZipFile('index_FO/DTOP_F_20130927.zip')
[a.read(x) for x in a.namelist() if 'opt_dtl_all.raw' in x]
r = [a.read(x) for x in a.namelist() if 'opt_dtl_all.raw' in x]
r = r[0]
r
pat = '"01"(.*)\r\n'
re.findall(pat,r)
r = re.findall(pat,r)
len(r)
[x.replace('"','') for x in r]
[y.split(',') for y in [x.replace('"','') for x in r]]
re.findall(pat,r)
get_ipython().magic(u'hist')
['Market','Marketname','Underlying','ExMonth','ExYear','strike','CALL_gross','CALL_net','CALL_netchange',\'CALL_TO','CALL_deal','CALL_settleprice','CALL_pricechange','PUT_gross','PUT_net','PUT_netchange','PUT_TO','PUT_deal','PUT_settleprice','PUT_pricechange']
['Market','Marketname','Underlying','ExMonth','ExYear','strike',\'CALL_gross','CALL_net','CALL_netchange',\'CALL_TO','CALL_deal','CALL_settleprice','CALL_pricechange',\'PUT_gross','PUT_net','PUT_netchange','PUT_TO','PUT_deal','PUT_settleprice','PUT_pricechange']
['Market','Marketname','Underlying','ExMonth','ExYear','strike',\'CALL_gross','CALL_net','CALL_netchange',\'CALL_TO','CALL_deal','CALL_settleprice','CALL_pricechange',\'PUT_gross','PUT_net','PUT_netchange','PUT_TO','PUT_deal','PUT_settleprice','PUT_pricechange']
get_ipython().magic(u'load index_future_option.py')
from pandas import *
import zipfile, re, urllib
from datetime import date


class indexoption():
	def __init__(self):
		pass
	def getoption(self):
		day = raw_input('enter the date code e.g. yyyymmdd :   ')
		print '\n'
		if not day:
			zipurl = 'http://www.hkex.com.hk/eng/stat/dmstat/OI/DTOP_F_%s.zip' % day
			urllib.urlretrieve(zipurl,'index_FO/'+day+'.zip')
			fname = 'index_FO/'+day+'.zip'
			a = zipfile.ZipFile(fname)
			for x in a.namelist():
				if 'opt_dtl_all.raw' in x:
					raw = a.read(x)
			pat = '"01"(.*)\r\n'
			r = re.findall(pat,raw)[0]
			data = [y.split(',') for y in [x.replace('"','') for x in r]]
			df =  DataFrame(data)
			colname = ['Market','Marketname','Underlying','ExMonth',\
			'ExYear','strike','CALL_gross','CALL_net',\
			'CALL_netchange','CALL_TO','CALL_deal','CALL_settleprice',\
			'CALL_pricechange','PUT_gross','PUT_net','PUT_netchange',\
			'PUT_TO','PUT_deal','PUT_settleprice','PUT_pricechange']
			df.columns = colname
			return df
idx = indexoption()
idx.getoption()
tp = idx.getoption()
tp
from pandas import *
import zipfile, re, urllib
from datetime import date


class indexoption():
	def __init__(self):
		pass
	def getoption(self):
		day = raw_input('enter the date code e.g. yyyymmdd :   ')
		print '\n'
		if day:
			zipurl = 'http://www.hkex.com.hk/eng/stat/dmstat/OI/DTOP_F_%s.zip' % day
			urllib.urlretrieve(zipurl,'index_FO/'+day+'.zip')
			fname = 'index_FO/'+day+'.zip'
			a = zipfile.ZipFile(fname)
			for x in a.namelist():
				if 'opt_dtl_all.raw' in x:
					raw = a.read(x)
			pat = '"01"(.*)\r\n'
			r = re.findall(pat,raw)[0]
			data = [y.split(',') for y in [x.replace('"','') for x in r]]
			df =  DataFrame(data)
			colname = ['Market','Marketname','Underlying','ExMonth',\
			'ExYear','strike','CALL_gross','CALL_net',\
			'CALL_netchange','CALL_TO','CALL_deal','CALL_settleprice',\
			'CALL_pricechange','PUT_gross','PUT_net','PUT_netchange',\
			'PUT_TO','PUT_deal','PUT_settleprice','PUT_pricechange']
			df.columns = colname
			return df
idx = indexoption()
tp = idx.getoption()
from pandas import *
import zipfile, re, urllib
from datetime import date


class indexoption():
	def __init__(self):
		pass
	def getoption(self):
		day = raw_input('enter the date code e.g. yyyymmdd :   ')
		print '\n'
		if day:
			zipurl = 'http://www.hkex.com.hk/eng/stat/dmstat/OI/DTOP_F_%s.zip' % day
			urllib.urlretrieve(zipurl,'index_FO/'+day+'.zip')
			fname = 'index_FO/'+day+'.zip'
			a = zipfile.ZipFile(fname)
			for x in a.namelist():
				if 'opt_dtl_all.raw' in x:
					raw = a.read(x)
			pat = '"(01".*)\r\n'
			r = re.findall(pat,raw)[0]
			data = [y.split(',') for y in [x.replace('"','') for x in r]]
			df =  DataFrame(data)
			colname = ['type','Market','Marketname','Underlying','ExMonth',\
			'ExYear','strike','CALL_gross','CALL_net',\
			'CALL_netchange','CALL_TO','CALL_deal','CALL_settleprice',\
			'CALL_pricechange','PUT_gross','PUT_net','PUT_netchange',\
			'PUT_TO','PUT_deal','PUT_settleprice','PUT_pricechange']
			df.columns = colname
			return df
date.today().strftime('%y%m%d')
date.today().strftime('%Y%m%d')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
a = zipfile.ZipFile(fname)
for x in a.namelist():
	if 'opt_dtl_all.raw' in x:
		raw = a.read(x)
pat = '("01".*)\r\n'
r = re.findall(pat,raw)
get_ipython().magic(u'run index_future_option.py')
fname ='index_FO/20131004.zip'
a = zipfile.ZipFile(fname)
for x in a.namelist():
	if 'opt_dtl_all.raw' in x:
		raw = a.read(x)
pat = '("01".*)\r\n'
r = re.findall(pat,raw)
data = [y.split(',') for y in [x.replace('"','') for x in r]]
df =  DataFrame(data)
colname = ['type','Market','Marketname','Underlying','ExMonth','ExYear','strike','CALL_gross','CALL_net','CALL_netchange','CALL_TO','CALL_deal','CALL_settleprice','CALL_pricechange','PUT_gross','PUT_net','PUT_netchange','PUT_TO','PUT_deal','PUT_settleprice','PUT_pricechange']
df.columns = colname

df
df.exMonth
df.ExMonth
df.index
df.columns[5:]
df.columns[6:]
df.columns[:6]
del df.columns[:6]
del df[df.columns[:6]]
df
df['maturity'] = df.ExMonth+df.ExYear
df
[1,2,4:7]
[1,2,[4:7]]
df.ix[:,[1,2,[4:7]]]
df.ix[:,[1,2]]
df.ix[:,[1,2,slice(6,21)]]
df
n = df.ix[:,6:]
n
n + df[2]
df[2]
df.iloc[2]
df['Underlying']
n+df['Underlying']
n.add(df['Underlying'])
n
n.append(df['Underlying'])
n
n.append(df['type'])
df['type']
Series(df['type'])
type(df.type)
n.append(df.type)
n.add(df.type)
n.append(df.type)
n.shape
n.join(df.type)
n.join(df.Underlying)
n
df
del df.maturity
del df['maturity']
df
df.drop('market')
df.drop('Market')
df
df.drop('type')
df
n = df.ix[:,6:]
n.apply(lambda x: x.astype(float))
n = n.apply(lambda x: x.astype(float))
n = n.join(df.Underlying)
n['mat'] = df.ExMonth + df.ExYear
n
n
n.ix[:,'strike':]
n.ix[:,'strike':'mat']
n
n.ix[:,'strike':'Underlying']
get_ipython().magic(u'run index_future_option.py')
idx
op = idx.getoption()
op
n
n.mat
n = n.set_index(['Underlying','mat'])
n
n['HSI']
n[['HSI']]
n[['HSI','OCT13']]
n['HSI','OCT13']
n.ix['HSI':]
n.ix[['HSI','OCT13']:]
n.ix['HSI','OCT13':]
n.ix['HSI':]
n[:4]
n.ix['HSI','OCT13']
n.ix[('HSI','OCT13')]
n
set(n.index)
n[('HSI','oCT13')]
n
n.index.set()
n.index.itemset
n.index.itemset()
n.index.levels
n.ix[('HSI','OCT13')]
n
n.ix[('HSI','OCT13'):]
n[:5]
n.ix[('HSI','OCT13')]
n.ix[('HSI','OCT13'),]
n.ix[('HSI','OCT13'),:]
n.ix[('HSI','OCT13'),:]
n.ix[('HSI','OCT13'):,:]
n.ix[('HSI','OCT13'),:]
n.levels
n.index.levels
n
n
n[('HSI','OCT13')]
u.ix[('HSI','OCT13'),:]
n.ix[('HSI','OCT13'),:]
n.xs[('HSI','OCT13')]
n.xs('OCT13',level='HSI')
n.sortlevel('Underlying')
n.sortlevel(['Underlying','mat'])
n.sortlevel('Underlying')
n.ix['HSI':'HSI']
n.ix[('HSI','OCT13'):('HSI','OCT13')]
n
n
n.xs(('HSI','OCT13'))
n['HSI']
n['OCT13']
n['Underlying']
n.reset_index
n.reset_index()
n = n.reset_index()
n.set_index(['Underlying','mat'])
n = n.set_index(['Underlying','mat'])
n.index
n.ix[['HSI','OCT13']]
n.ix[['HSI','OCT13']:]
n.ix[['HSI','OCT13']:['HSI','OCT13']]
n.xs(['HSI','OCT13'])
n.ix[('HSI','OCT13')]
n.ix[('HSI','OCT13'):]
n.sort_index(0)
n = n.sort_index(0)
n.ix[('HSI','OCT13')]
n.sortlevel(0)
sn = n.sortlevel(0)
sn.ix[('HSI','OCT13')]
sn == n
sn is n
sn is n.ix[('HSI','OCT13')]
si = n.ix[('HSI','OCT13')]
si
si == sn
sn is si
sn in si
si == sn
si
si[3] = sn[3]
si.index
si.ix[3] == sn.ix[3]
si
si.sort('strike')
si = si.sort('strike')
si
si[4]
si.ix[3]
si.ix[3] = sn.ix[3]
si.ix[4] == sn.ix[4]
sn.index
sn
n
n
n
si = n.sort_index(0)
sn = n.sortlevel(0)
si
sn
si == sn
si is sn
si.index == sn.index
si.index eq sn.index
si <> sn
si.index <> sn.index
sn
sn[['HSI','OCT13']]
sn[('HSI','OCT13')]
sn.index
sn.ix[('HSI','OCT13')]
hsi = sn.ix[('HSI','OCT13')]
hsi.set_index('strike')
c = hsi.set_index('strike')
c['CALL_net','PUT_net']
c[['CALL_net','PUT_net']]
c[['CALL_net','PUT_net']].plot()
c[['CALL_net','PUT_net']].plot(kind='bar')
c[['CALL_net','PUT_net']].plot(kind='bar',x_compat=1)
c[['CALL_net','PUT_net']].plot(kind='bar',x_compat=TRUE)
c[['CALL_net','PUT_net']].plot(kind='bar',x_compat=True)
c[['CALL_net','PUT_net']].plot(kind='bar')
c.columns.apply(lambda x: x.upper())
[x.upper() for x in c.columns]
c.columns = [x.upper() for x in c.columns]
c
n
n.sortlevel(1)
df
df.sortlevel(1)
df.sortlevel(1)
df.sort_index(1)
c
c[['CALL_NET','PUT_NET']].plot(kind='bar',stack=True)
c[['CALL_NET','PUT_NET']].plot(kind='bar',stacked=True)
n
sn
sn.ix[('HSI','NOV13')]
nextm = sn.ix[('HSI','NOV13')]
nextm
nm = nextm.sortlevel(0)
nm
nm.set_index('strike')
nm = nm.set_index('strike')
nm[['CALL_NET','PUT_NET']]
nm
nm[['CALL_net','PUT_net']]
nm[['CALL_net','PUT_net']].plot(kind='bar',stacked=1)
df
df.rename('Market':'MARKET')
df.rename(columns={'Market':'MARKET'})
df
get_ipython().magic(u'run index_future_option.py')
idx
df = idx.getoption()
get_ipython().magic(u'run index_future_option.py')
df = idx.getoption()
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'load index_future_option.py')
get_ipython().magic(u'load index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'run index_future_option.py')
m = idx.getoption()
m
m.set_index(['EXTIME','UNDERLYING'])
sm =m.set_index(['EXTIME','UNDERLYING'])
sm.sortlevel(0)
sm = sm.sortlevel(0)
sm[['OCT13','HSI']]
sm.index
sm.ix[('OCT13','HSI')]
get_ipython().magic(u'run index_future_option.py')
get_ipython().magic(u'logstop')
