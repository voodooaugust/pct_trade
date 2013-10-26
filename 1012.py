# IPython log file

get_ipython().magic(u'cd E:\\Users\\august\\Documents\\google\\pct_trade/')
get_ipython().magic(u'load 1002.py')
get_ipython().magic(u'load 1012.py')
# IPython log file

get_ipython().magic(u'cd E:\\Users\\august\\Documents\\google\\pct_trade/')
import histdata as hd
get_ipython().magic(u'logstart 1012.py')
cs = [836, 777, 3888, 2333, 1211, 2866, 6863, 3337, 1988, 6030, 489]
y = hd.yahoofin()
dl = {x:y.getDATA(x) for x in cs}
d1 = {str(x):dl[x].ac.pct_change().dropna() for x in dl}
d1
d1
for x in d1:
    expanding_mean(x).plot()
for x in d1:
    expanding_mean(d1[x]).plot()
for x in d1:
    expanding_mean(d1[x]).plot(legand=1)
for x in d1:
    expanding_mean(d1[x]).plot(legend=1)
expanding_mean(d1['836']).plot()
DataFrame(d1)
expanding_mean(DataFrame(d1)).plot()
expanding_mean(DataFrame(d1)).plot(legend=0)
expanding_kurt(DataFrame(d1)).plot(legend=0)
d1['2333']
expanding_kurt(d1['2333']).plot()
d1['2333'].kurt()
d1['2333'].skew()
d1['2333'].plot(kind='kde')
v1 = DataFrame(d1)
v1
v1.skew()
DataFrame({'skew':Series(v1.skew()),'kurt':Series(v1.kurt())})
c1 = DataFrame({'skew':Series(v1.skew()),'kurt':Series(v1.kurt())})
import matplotlib.pyplot as plt
area = v1.var()
plt.scatter(c1.skew,c1.kurt,s=area, alpha(0.5))
import matplotlib.pyplot as plt
area = v1.var().values
plt.scatter(c1.skew.values,c1.kurt.values,s=area, alpha(0.5))
c1.skew.value
c1.skew.values
c1.skew
c1
c1.skew
c1['skew']
import matplotlib.pyplot as plt
area = v1.var()
plt.scatter(c1['skew'],c1['kurt'],s=area, alpha(0.5))
v1.var()
v1.var().toarray()
import matplotlib.pyplot as plt
area = v1.var()
plt.scatter(c1['skew'],c1['kurt'],s=area, alpha=0.5)
import matplotlib.pyplot as plt
area = v1.var()*100
plt.scatter(c1['skew'],c1['kurt'],s=area, alpha=0.5)
import matplotlib.pyplot as plt
area = v1.var()*10000
plt.scatter(c1['skew'],c1['kurt'],s=area, alpha=0.5)
v1.var
v1.var()
import matplotlib.pyplot as plt
area = v1.var()*1000000
plt.scatter(c1['skew'],c1['kurt'],s=area, alpha=0.5)
v1
c1
del c1['2333']
get_ipython().magic(u'logstart 1013.py')
get_ipython().magic(u'logstop')
# IPython log file

get_ipython().magic(u'cd E:\\Users\\august\\Documents\\google\\pct_trade/')
import histdata as hd
get_ipython().magic(u'logstart 1012.py')
cs = [836, 777, 3888, 2333, 1211, 2866, 6863, 3337, 1988, 6030, 489]
y = hd.yahoofin()
dl = {x:y.getDATA(x) for x in cs}
d1 = {str(x):dl[x].ac.pct_change().dropna() for x in dl}
d1
d1
for x in d1:
    expanding_mean(x).plot()
for x in d1:
    expanding_mean(d1[x]).plot()
for x in d1:
    expanding_mean(d1[x]).plot(legand=1)
for x in d1:
    expanding_mean(d1[x]).plot(legend=1)
expanding_mean(d1['836']).plot()
DataFrame(d1)
expanding_mean(DataFrame(d1)).plot()
expanding_mean(DataFrame(d1)).plot(legend=0)
expanding_kurt(DataFrame(d1)).plot(legend=0)
d1['2333']
expanding_kurt(d1['2333']).plot()
d1['2333'].kurt()
d1['2333'].skew()
d1['2333'].plot(kind='kde')
v1 = DataFrame(d1)
v1
v1.skew()
DataFrame({'skew':Series(v1.skew()),'kurt':Series(v1.kurt())})
c1 = DataFrame({'skew':Series(v1.skew()),'kurt':Series(v1.kurt())})
d1
v1
d1
d1
expanding_skew(DataFrame(d1)).plot()
expanding_kurt(d1['3888']).plot()
import matplotlib.pyplot as plt
d1
c1 = {'skew':d1.skew(),'kurt':d1.skew(),'var':d1.var()}
c1 = {'skew':d1.skew(),'kurt':d1.kurt(),'var':d1.var()}
d1.kurt()
d1
d1 = DataFrame(d1)
c1 = {'skew':d1.skew(),'kurt':d1.kurt(),'var':d1.var()}
c1
c1 = DataFrame({'skew':d1.skew(),'kurt':d1.kurt(),'var':d1.var()})
c1
d1
d1.idxmax()
d1.idxmin()
d2 = DataFrame()
for i, x in d1.idxmin().iterrow():
    if len(d1[str(i)]) < len(d1.ix[x:,i]):
        d2[str(i)] = d1.ix[x:,i]
d2 = DataFrame()
for i, x in d1.idxmin().iterrows():
    if len(d1[str(i)]) < len(d1.ix[x:,i]):
        d2[str(i)] = d1.ix[x:,i]
d2 = DataFrame()
for i, x in d1.idxmin().iteritems():
    if len(d1[str(i)]) < len(d1.ix[x:,i]):
        d2[str(i)] = d1.ix[x:,i]
d2
d2 = DataFrame()
for i, x in d1.idxmin().iteritems():
    if len(d1[str(i)]) < len(d1.ix[x:,i]):
        d2[str(i)] = d1.ix[x:,str(i)]
d2
d2 = DataFrame()
for i, x in d1.idxmin().iteritems():
    if len(d1[str(i)]) < len(d1.ix[x:,i]):
        d2[str(i)] = d1.ix[str(x):,str(i)]
d2
d1
d1['2010-09-07']
d1
d1['2010-01-04']
d1
d1.reset_index()
d1.ix[:,1:].idxmax()
d3 = d1.reset_index()
d3.ix[:,1:].idxmax()
d1
d2
d3
d1 = d1.reset_index()
d2 = DataFrame()
for i, x in d1.idxmin().iteritems():
    if len(d1[str(i)]) < len(d1.ix[x:,i]):
        d2[str(i)] = d1.ix[x:,str(i)]
d2
d1.idxmax()
d1.idxmax()d1
d1
d1 = d1.set_index('index')
d1
for i, x in d1.iteritems():
    print i.type
d1
d2 = DataFrame()
for i, x in d1.idxmin().iteritems():
    if len(d1[str(i)]) < len(d1.ix[x:,i]):
        d2[str(i)] = d1.ix[str(x):,str(i)]
d2
d1.ix['2013-10-02':]
d1.ix[date('2013-10-02'):]
from datetime import date
d1.ix[date('2013-10-02'):]
d1.index
d1.ix['2013-07-12']
d1.ix[10]
d1.idxmax()
d1.idxmax().index
d1.index = d1.index.apply(lambda x:str(x))
d1
d1.index
for i, x in d1.idxmin():
    print d1.ix[x]
d1['07/23/2013':]
d1[datetime(2013,7,23):]
d1
d1 = d1.reset_index()
d1['index'].apply(lambda x:x.date())
d1 = d1.set_index('index')
d1
d1[date(2013,7,23):]
d1.idxmin()
d1.idxmin().date()
d1.idxmin().ix[2]
d1.ix[d1.idxmin().ix[2]:]
d1.ix[d1.idxmin().ix[2]:,'2333']
for i , x in d1.idxmin():
    print type(x)
type(d1.idxmin())
i1 = d1.idxmin()
i1
for i ,each in i1:
    print i
    
i1
for i, x in i1.iteritems():
    print i
d2 = DataFrame()
for i, x in i1.iteritems():
    d2[str(i)] = d1.ix[date(x),str(i)]
d2
d2 = DataFrame()
for i, x in i1.iteritems():
    d2[str(i)] = d1[str(i)].ix[date(x)]
d2
d2 = DataFrame()
for i, x in i1.iteritems():
    d2[str(i)] = d1[str(i)].ix[x]
d2
for i, x in i1.iteritems():
    print date(x)
i1
d1
for i, x in i1:
    print x
date(2013,7,23)
i1[2]
i1[2] == date(2011,9,26)
i2[str(2333)]
i1[str(2333)]
d2 = DataFrame()
for i, x in i1.iteritems():
    d2[str(i)] = d1[str(i)].ix[i1[str(i):]
d2
d2 = DataFrame()
for i, x in i1.iteritems():
    d2[str(i)] = d1[str(i)].ix[i1[str(i)]:]
d2
d1['3888'].ix[i1['3888']]
d1['3888'].ix[i1['3888']:]
d1['3888'].ix[i1['3888']:]
d2
d2 = DataFrame()
for i, x in i1.iteritems():
    d2.join(d1[str(i)].ix[i1[str(i)]:])
d2
i1 = d1.idxmin()
d2 = DataFrame()
for i, x in i1.iteritems():
    d2.join(d1[str(i)].ix[i1[str(i)]:],how='outer')
d2
d1
d1
i1['6869']
i1['6863']
d1[i1['6863']:]
s1 = d1['2333']
s2 = d1['6863']
s1
s2
s2 = s2[-9:]
s2
merge(s1,s2,how='outer')
concat([s1,s2],axis=1)
concat([s1,s2],axis=1).tail(20)
for i, x in i1.iteritems():
    d1[str(i)] = d1[str(i)].ix[i1[str(i)]:]
d1
d3
d3
d3
d3 = d3.set_index('index')
d3
d1
d1
expanding_kurt(d1).plot()
expanding_skew(d1).plot()
i1
d1['1988']
d1['1988'].min()
d1['1988'].cumsum()
d1['1988'].cumsum().plot()
d1[d1['1988']argmin()]['1988'].cumsum().plot()
d1[d1['1988'].argmin():]['1988'].cumsum().plot()
v1 = d1[d1['1988'].argmin():]
v1
v1['1988'].cumsum().plot()
d1
d1
{'skew':d1.skew(),'kurt':d1.kurt()}
v1 = DataFrame({'skew':d1.skew(),'kurt':d1.kurt(),'var':d1.var()})
v1
plt.scatter(v1.kurt,v1.skew,area=v1.var,alpha=0.5)
v1
v1 = v1.fillna(0)
v1
plt.scatter(v1.kurt,v1.skew,area=v1.var,alpha=0.5)
plt.scatter(v1.kurt,v1.skew,s=v1.var,alpha=0.5)
plt.scatter(v1.kurt,v1.skew,s=v1.var*10000,alpha=0.5)
v1.var*1000
v1.var
plt.scatter(v1['kurt'],v1['skew'],s=v1['var']*10000,alpha=0.5)
plt.scatter(v1['kurt'],v1['skew'],s=v1['var']*100000,alpha=0.5)
plt.scatter(v1['kurt'],v1['skew'],s=v1['var']*100000,alpha=0.5)
for label, x, y in zip(v1.index.values,v1['kurt'],v2['skew']):
    plt.annotate(label,xy = (x,y))
plt.scatter(v1['kurt'],v1['skew'],s=v1['var']*100000,alpha=0.5)
for label, x, y in zip(v1.index.values,v1['kurt'],v1['skew']):
    plt.annotate(label,xy = (x,y))
plt.scatter(v1['kurt'],v1['skew'],s=v1['var']*100000,alpha=0.5,c=d1.mean())
for label, x, y in zip(v1.index.values,v1['kurt'],v1['skew']):
    plt.annotate(label,xy = (x,y))
v1
d1
d1['1211'].cumsum().plot()
concat([v1,{'mean':d1.mean()}],axis=1)
v1.join(d1.mea())
v1.join(d1.mean())
v1.join({'mean':d1.mean()})
p1
p1 = {'mean':d1.mean()}
concat([v1,p1],axis=1)
v1
v1['mean'] = d1.mean()
v1
v1
v1.sort('mean',ascending=0)
v1.sort('mean',ascending=0, inplace=1)
v1
plt.scatter(x=v1['kurt'],y=v1['skew'],c=v1['mean'],s=v1['var'],cmap=plt.cm.get_cmap('BrBG'))
plt.scatter(x=v1['kurt'],y=v1['skew'],c=v1['mean'],s=v1['var']*100000,cmap=plt.cm.get_cmap('BrBG'))
plt.scatter(x=v1['kurt'],y=v1['skew'],c=v1['mean'],s=v1['var']*100000,cmap=plt.cm.get_cmap('BrBG'))
plt.annotate(v1.index.values,xy=(v1['kurt'],v1['skew']))
zip(v1.index.values,v1['kurt'],v1['skew'])
plt.scatter(v1['kurt'],v1['skew'],s=v1['var']*100000,alpha=0.5,c=d1.mean(),cmap=plt.cm.get_cmap('BrBG'))
for label, x, y in zip(v1.index.values,v1['kurt'],v1['skew']):
    plt.annotate(label,xy = (x,y),xytext = (-20,20))
plt.scatter(v1['kurt'],v1['skew'],s=v1['var']*100000,alpha=0.5,c=d1.mean(),cmap=plt.cm.get_cmap('BrBG'))
for label, x, y in zip(v1.index.values,v1['kurt'],v1['skew']):
    plt.annotate(label,xy = (x,y))
v1
d1
d1.plot(kind='kde')
d1.fillna(0).plot(kind='kde')
d1.dropna().plot(kind='kde')
ax = d1.dropna().plot(kind='kde')
for l, x, y in zip(d1.index.values,d1.mean(),d1.mode()):
    ax.annotate(l, xy=(x,y))
ax = d1.dropna().plot(kind='kde')
for l, x, y in zip(d1.index.values,d1.mean(),d1.kurt().sort(ascending=0)):
    ax.annotate(l, xy=(x,y))
p1=d1.kurt().sort(ascending=0)
p1
p1
d1.kurt()
d1.kurt().fillna(0)
d1.kurt().fillna(0).sort(ascending=1)
d1.kurt().fillna(0)
d1.kurt().fillna(0).rank()
d1.kurt().fillna(0).sort(acsending=1)
d1.kurt().fillna(0).sort(ascending=1)
d1.kurt().fillna(0).order(ascending=1)
d1.kurt().fillna(0).order(ascending=0)
ax = d1.dropna().plot(kind='kde')
for l, x, y in zip(d1.index.values,d1.mean(),d1.kurt().rank(ascending=0)):
    ax.annotate(l, xy=(x,y))
ax = d1.dropna().plot(kind='kde')
for l, x, y in zip(d1.columns,d1.mean(),d1.kurt().rank(ascending=0)*4):
    ax.annotate(l, xy=(x,y))
d1.kurt().rank(ascending=0)
d1.kurt().rank(ascending=1)
d1['777'].plot(kind='kde')
d1['777'].dropna().plot(kind='kde')
d
d1
ax = d1['2333'].plot(kind='kde')
ax = d1['2333'].dropna().plot(kind='kde')
ax.subplot(112)
ax.subplot(221)
axs = plt.subplot(nrows=2,ncols=2)
plt.subplot(nrows=2,ncols=2)
plt.subplots(nrows=2,ncols=2)
a = plt.subplots(nrows=2,ncols=2)
d1['6030'].dropna().plot(kind='kde',ax = a[0,0])
f , a = plt.subplots(nrows=2,ncols=2)
d1['6030'].dropna().plot(kind='kde',ax = a[0,0])
d1['836'].dropna().plot(kind='kde',ax=a[0,1])
f,a = plt.subplots(nrows=2,ncols=2)
d1['6030'].dropna().plot(kind='kde',ax = a[0,0])
d1['836'].dropna().plot(kind='kde',ax=a[0,1])
v1
f,a = plt.subplots(nrows=2,ncols=2)
d1['6030'].dropna().plot(kind='kde',ax = a[0,0])
d1['836'].dropna().plot(kind='kde',ax=a[0,1])
d1['777'].dropna().plot(kind='kde',ax=[1,0])
f,a = plt.subplots(nrows=2,ncols=2)
d1['6030'].dropna().plot(kind='kde',ax = a[0,0])
d1['836'].dropna().plot(kind='kde',ax=a[0,1])
d1['777'].dropna().plot(kind='kde',ax=a[1,0])
f,a = plt.subplots(nrows=2,ncols=2)
d1['6030'].dropna().plot(kind='kde',ax = a[0,0])
d1['836'].dropna().plot(kind='kde',ax=a[0,1])
d1['777'].dropna().plot(kind='kde',ax=a[1,0])
d1['3888'].dropna().plot(kind='kde',ax=a[1,1])
f,a = plt.subplots(nrows=2,ncols=2)
d1['6030'].dropna().plot(kind='kde',ax = a[0,0])
d1['836'].dropna().plot(kind='kde',ax=a[0,1])
d1['6863'].dropna().plot(kind='kde',ax=a[1,0])
d1['3888'].dropna().plot(kind='kde',ax=a[1,1])
f,a = plt.subplots(nrows=2,ncols=2)
d1['489'].dropna().plot(kind='kde',ax = a[0,0])
d1['836'].dropna().plot(kind='kde',ax=a[0,1])
d1['6863'].dropna().plot(kind='kde',ax=a[1,0])
d1['3888'].dropna().plot(kind='kde',ax=a[1,1])
d1.dropna().plot(kind='kde')
f,a = plt.subplots(nrows=2,ncols=2)
d1['489'].dropna().plot(kind='kde',ax = a[0,0])
d1['836'].dropna().plot(kind='kde',ax=a[0,1])
d1['3337'].dropna().plot(kind='kde',ax=a[1,0])
d1['1211'].dropna().plot(kind='kde',ax=a[1,1])
d1.applymap(round)
d1.applymap(round).count()
d1.applymap(round).mode()
import scipy as sp
d1.applymap(sp.stats.norm)
d1.dropna().applymap(sp.stats.norm)
d1.dropna().apply(sp.stats.norm)
d1.dropna().apply(sp.stats.norm).plot()
d1.dropna().apply(sp.stats.norm.cdf).plot()
sp.stats.norm.cdf(d1['2333'])
sp.stats.norm.cdf(d1['2333'].dropna()).plot()
plt.plot(sp.stats.norm.cdf(d1['2333'].dropna()))
d1
v1
d1['1988'].dropna().plot(kind='kde')
len(d1.T)
f, a = plt.subplots(nrows=11,ncols=1)
i = 0
for each in d1:
    i+=1
    d1[each].dropna().plot(kind='kde',ax=a[i,0])
for each in d1:

    d1[each].dropna().plot(kind='kde')
d1
for each in d1:
    expanding_mean(d1[each].dropna()).plot()
get_ipython().magic(u'hist')
get_ipython().magic(u'dir')
get_ipython().system(u'dir /on ')
import qfin as qf
qf.m2()
qf.m2('')
reload(qf)
qf.m2()

reload(qf)
qf.m2('')
a = []
type(a) is list
reload(hd)
reload(hd)
y = hd.yahoofin()
c = [836,1071,991,902]
y.dataoo(c)
d = y.dataoo(c)
d
reload(hd)
y = hd.yahoofin()
y.dataoo(c)
y.d
y.d['1071']
y.d['1071'].tail()
for x in y.d:
    print x
for x in y.d:
    y.d[x].where(volume >0).ac.pct_change()
for x in y.d:
    me = y.d[x]
    print me[me['volume'] > 0].ac.pct_change().dropna()
v1 = {}
for x in y.d:
    me = y.d[x]
    s = me[me['volume'] > 0].ac.pct_change().dropna()
    v1.update({x:s})
v1 = DataFrame(v1)
v1
reload(hd)
y=hd.yahoofin()
y.dataoo(c)
y.kurtskew()
reload(hd)
y=hd.yahoofin()
y.dataoo(c)
y.kurtskew()
y.d
type(y.d)
reload(hd)
y=hd.yahoofin()
y.dataoo(c)
y.kurtskew()
reload(hd)
y=hd.yahoofin()
y.dataoo(c)
y.kurtskew()
reload(hd)
y=hd.yahoofin()
y.dataoo(c)
y.kurtskew()
reload(hd)
y=hd.yahoofin()
y.dataoo(c)
y.kurtskew()
reload(hd)
y=hd.yahoofin()
y.dataoo(c)
y.kurtskew()
y.v1
t
y.v2
c = [1112,836,1071,991,902,6030,6837,2333,3888,777]
reload(hd)
y=hd.yahoofin()
y.dataoo(c)
y.kurtskew()
v1
y.v1
c
reload(hd)
y = hd.yahoofin()
y.getDATA(c)
reload(hd)
y = hd.yahoofin()
y.dataoo(c)
y.kurtskew()
reload(hd)
y = hd.yahoofin()
y.dataoo(c)
y.kurtskew()
y.v1
y.d2
y.v2
yv1
y.v1
reload(hd)
reload(hd)
y =hd.yahoofin()
v1
y.v1
c
c.drop('2333')
del c['2333']
del c[-2]
c
c.remove(2333)
c
c.extend(3888)
c.append(3888)
c
y.dataoo(c)
y.kurtskew()
reload(hd)
y = hd.yahoofin()
y.dataoo(c)
y.kurtskew()
reload(hd)
y = hd.yahoofin()
y.dataoo(c)
y.kurtskew()
reload(hd)
y = hd.yahoofin()
y.dataoo(c)
y.kurtskew()
y.v1.idxmin()
d= {}
for i, x in y.v1.idxmin().iteritems():
    d.update({i:y.v1[i].ix[x:]})
d = DataFrame(d)
    
d
d.tail()
y.v1 = d
reload(hk)
reload(hd)
y = hd.yahoofin()

y.plotkurtskew(d)
reload(hd)
y = hd.yahoofin()
y.plotkurtskew(d)
reload(hd)
y = hd.yahoofin()
reload(hd)
y = hd.yahoofin()
y.plotkurtskew(d)
d
y.v1
v1
del v1
v2
v1
d
d.std()
d.std()*100
reload(hd)
y = hd.yahoofin()
y.plotkurtskew(d)
reload(hd)
y = hd.yahoofin()
y.plotkurtskew(d)
d
d.head()
d.dropna()
c
c.append(168)
c
y.dataoo(c)
y.kurtskew()
y.d
y.v1
d=y.v1
for i, x in d.idxmin().iteritems():
    d[i] = d[i].ix[x:]
d
d.head()
d.tail()
y.v1.idxmin()
d = y.v1
d
y.v1
d
d
len(d)
y.dataoo(c)
d=y.v1.copy()
d
y.v1
y.v1
y.d
y.v1
d.dropna()
for x in d:
    d[x] = d[x].dropna()
d
d.head()
d.count()
d.mean()
d.kurt()
y.plotkurtskew(d)
get_ipython().magic(u'hist')
