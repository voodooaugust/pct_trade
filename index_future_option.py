from pandas import *
import zipfile, re, urllib
from datetime import date


class indexoption():
	def __init__(self):
		self.day = date.today().strftime('%Y%m%d')
	def getoption(self):
		day = raw_input('enter the date code e.g. yyyymmdd :   ')
		if not day:
			day = '20131004'
			print 'the default day is 20131004'
		elif day == 'today':
			day = self.today
		fname = 'index_FO/'+day+'.zip'
		try:
			with open(fname): pass
		except IOError:
			print 'file will be created at %s ' % fname
			zipurl = 'http://www.hkex.com.hk/eng/stat/dmstat/OI/DTOP_F_%s.zip' % day
			urllib.urlretrieve(zipurl,'index_FO/'+day+'.zip')
		a = zipfile.ZipFile(fname)
		for x in a.namelist():
			if 'opt_dtl_all.raw' in x:
				raw = a.read(x)
		pat = '("01".*)\r\n'
		r = re.findall(pat,raw)
		data = [y.split(',') for y in [x.replace('"','') for x in r]]
		df =  DataFrame(data)
		colname = ['type','Market','Marketname','Underlying','ExMonth','EXTIME','strike','CALL_gross','CALL_net','CALL_netchange','CALL_TO','CALL_deal','CALL_settleprice','CALL_pricechange','PUT_gross','PUT_net','PUT_netchange','PUT_TO','PUT_deal','PUT_settleprice','PUT_pricechange']
		df.columns = [x.upper() for x in colname]
		df.EXTIME= df.EXMONTH + df.EXTIME
		m = df.ix[:,'EXTIME':]
		m = m.join(df['UNDERLYING'])
		m = m.set_index(['UNDERLYING','EXTIME'])
		m = m.sortlevel(0)
		m = m.apply(lambda x:x.astype(float))
		return m

idx = indexoption()
