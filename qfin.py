from pandas import *
from datetime import date, datetime, timedelta
import zipfile, re, urllib, os

# set displat columns
pandas.set_option('display.max_columns', 30)

def methond1():
	try:
		from histdata import yahoofin
		from quant import df
	except ImportError:
		print 'can not import histdata'
	period = 20
	_, bt = df(period)
	codeset = [str(y[0]).zfill(4) for y in bt.index]
	yh = yahoofin()
	for x in codeset:
		fname = 'yahoofin/' + x + '.csv'
		try:
			ok = datetime.fromtimestamp(os.path.getmtime(fname)).date() == date.today()
		except:
			yh.getYFIN(x)
		else:
			if not ok:
				yh.getYFIN(x)
	return bt

def m2(cs):
	try:
		import histdata as hd
		import matplotlib.pyplot as plt
	except:
		print 'error when import !!!'
	if not cs:
		cs = [836, 777, 3888, 2333, 1211, 2866, 6863, 3337, 1988, 6030, 489]
		print cs
	y = hd.yahoofin()
	y.dataoo(cs)
	y.kurtskew()

	v1 = y.v1
	n = {}
	for i, x in v1.idxmin().iteritems():
		if len(v1[i].ix[x:]) < .3*len(v1[i]):
			n.update({i:v1[i].ix[x:]})
		else:
			n.update({i:v1[i]})
	n = DataFrame(n)
	plt.figure()
	y.plotkurtskew(n)
	return y
def m3(x):
	
	y = x
	v1 = y.v1.copy()

	t={}
	for i, x in v1.idxmin().iteritems():
		t.update({i:v1[i].ix[x:]})
	t = DataFrame(t)
	y.plotkurtskew(t)
	return v1
