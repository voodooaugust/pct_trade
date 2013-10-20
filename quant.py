from __future__ import division
from pandas import *
import matplotlib.pyplot as plt
import numpy as np
import os

pandas.set_option('display.max_columns',30)

class master(DataFrame):
	def __init__(self):
		print 'initilize the master dataframe'
	def printme(self):
		pass

dfout = read_csv('df_main.csv',index_col=0)
dfout = dfout[['code','OUT_STANDING']]
dflist = []
def getTOP_TRADE(df, dfout):
	mdf = merge(df,dfout)
	mdf['pt'] = mdf.SH_TRADE / mdf.OUT_STANDING * 100
	mdf['mv'] = mdf.OUT_STANDING * mdf.turn / mdf.SH_TRADE
	col = ['code','name','SH_TRADE','OUT_STANDING','turn','pt','mv']
	mdf = mdf[col]
	mdf = mdf.sort('pt',ascending=0)
	mdf = mdf.set_index('code')
	return mdf[:50]
def readDF():
	dflist = []
	for each in os.listdir('stock_dataframe/'):
		filename = 'stock_dataframe/' + each
		df = read_csv(filename,thousands=',')
		dflist.append(getTOP_TRADE(df,dfout))
	return dflist
def updateQOUTATION():
	from pct_trade import qoutation
	print 'finish import'
	q = qoutation()
	print 'create instance'
	q.updateQoutation()
def df(period):
	folder = 'stock_dataframe//'
	files = os.listdir(folder)
	dflist = []
	dfout = read_csv('df_main.csv',index_col=0)
	for each in files[-period:]:
		print 'filename : %s ' % each
		fullname = folder + each
		df = read_csv(fullname, thousands=',')
		df = df[['code','name','SH_TRADE','turn','close']]
		mdf = merge(df,dfout)
		mdf['pt'] = mdf.SH_TRADE / mdf.OUT_STANDING*10000
		mdf.pt = mdf.pt.apply(round,0)
		mdf['vwap'] = mdf.turn / mdf.close
		mdf['mv'] = mdf.close*mdf.OUT_STANDING / 1000000
		mdf.mv = mdf.mv.apply(round,0)
		mdf = mdf[mdf.mv > 4000]
		dflist.append(mdf)
	# building merged dataframe
	master = dflist[0]
	master = master[['code','mv','pt']]
	master.columns = ['code','mv','pt_0']
	for i in range(len(dflist)-1):
		df = dflist[i+1][['code','pt']]
		newcol = ['code','pt_'+str(i+1)]
		df.columns = newcol
		master = merge(master, df, on='code')
	master = master.set_index(['code','mv'])
	print 'the master dataframe :'
	master['avg'] = master.apply(np.mean,axis=1)
	master = master.sort('avg',ascending=0)
	master = master[:40]
	# master dataframe is the result of pct trade
	print master.ix[:,-9:]
	print 'the current breakthrough of trade: '
	bt = master[master.iloc[:,-2] > master.iloc[:,-1]]
	print bt.ix[:,-9:]
	master.to_csv('trade_result.csv')
	return master, bt


# after construct the dataframe list
# build a time serie for indivisual stock
def ts():
	folder = 'stock_dataframe//'
	files = os.listdir(folder)
	ndf = df()
	for ele in ndf:
		temp = ele.set_index('code')
		print 'building time series for each dataframe %s' % ele
		print ' the new index is : '
		print temp.columns
		print len({x:y for x, y in temp.iterrows()})

if __name__ == '__main__':
	updateQOUTATION()
	df20 = df(20)