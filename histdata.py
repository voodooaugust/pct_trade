import urllib
from pandas import *
from datetime import date, timedelta
import os
import matplotlib.pyplot as plt

class yahoofin():
	def __init__(self):
		self.period = 500
		self.pathfolder = os.path.dirname(os.path.abspath(__file__))
		self.d = {}
		self.v1 = DataFrame()
		self.v2 = DataFrame()
		print ' v1 for pct_change \n v2 for statistics result'
	def getDATA(self,code):
		name = str(code).zfill(4)
		url = 'http://ichart.finance.yahoo.com/table.csv?s=%s.HK&a=00&b=1&c=2010&g=d&ignore=.csv' % name
		df = read_csv(url,thousands=',')
		df.Date = to_datetime(df.Date).apply(lambda x:x.date())
		df = df.set_index('Date')
		df = df.sort_index()
		df.rename(columns={'Adj Close':'ac'},inplace=1)
		df.columns = [x.lower() for x in df.columns]
		print 'save the file to %s\\yahoodata\\%s' % (self.pathfolder , name)
		df.to_csv(self.pathfolder+'/yahoodata/'+name+'.csv')
		return df
	def dataoo(self,ls):
		d = {}
		for x in ls:
			d.update({str(x).zfill(4):self.getDATA(x)})
		self.d =d
		return d
	def kurtskew(self):
		if self.d:
			d = self.d
			v1 = {}
			print ' \n\n\n selection critiria volume > 0 and dropna()\n'
			for each in d:
				me = d[each]
				s = me[me['volume'] > 0 ].ac.pct_change().dropna()
				v1.update({each:s})
			v1 = DataFrame(v1)
			v2 = {'kurt':v1.kurt(),'skew':v1.skew(),'std':v1.std(),'mean':v1.mean()}
			v2 = DataFrame(v2)
			plt.scatter(v2['skew'],v2['kurt'],s=v2['std']*(10**4),alpha=0.5)
			for label, x, y in zip(v2.index.values, v2['kurt'],v2['skew']):
				plt.annotate(label,xy=(y,x))

			self.v1, self.v2 = v1,v2

		else:
			print 'no data in the object '
	def plotkurtskew(self,d1):
		v1 = {}
		print 'the idxmin :::: \n'
		print d1.idxmin(skipna=1)
		for i, x in d1.idxmin().iteritems():
			v1.update({i:d1[i].ix[x:]})
		v1 = DataFrame(v1)
		v2 = {'kurt':v1.kurt(),'skew':v1.skew(),'std':v1.std(),'mean':v1.mean()}
		v2 = DataFrame(v2)
		print 'kurt and skew statistics summary\n'
		print v2
		plt.scatter(v2['skew'],v2['kurt'],s=v2['std']*(10**4),alpha=0.5)
		for label, x, y in zip(v2.index.values, v2['kurt'],v2['skew']):
			plt.annotate(label,xy=(y,x))
		return v2
	def recoveryrate(self,ls):
		d = self.dataoo(ls)
		print 'historical statistics kurt and skew'
		self.kurtskew()
		plt.figure()
		print '\n\nthe recovery after max drop \n'
		result = self.plotkurtskew(self.v1)
		return result