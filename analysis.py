from __future__ import division
from pandas import *
import numpy as np
import os

class analysis:
	def __init__(self):
		# init the cap size group
		self.CAPGROUP = ['s','m','l']
	def PARSE_PCT(self,filelist):
		pass
	def updateQOUTATION(self):
		from pct_trade import qoutation
		print 'finish import'
		q = qoutation()
		print 'create instance'
		q.updateQoutation()
	# define period as the time slot of dataset, and return the list of dataframe
	def importdata(self, period):
		folder = 'stock_dataframe//'
		files = os.listdir(folder)
		dfout = read_csv('df_main.csv',index_col=0)
		# dim a list of data frame
		dflist, ptlist= [], []
		for each in files[-period:]:
			print 'import filename : %s ' % each
			fullname = folder + each
			df = read_csv(fullname, thousands=',')
			df = df[['code','name','SH_TRADE','turn','close']]
			mdf = merge(df,dfout)
			mdf['pt'] = mdf.SH_TRADE / mdf.OUT_STANDING*10000.
			mdf.pt = mdf.pt.apply(round,0)
			mdf['vwap'] = mdf.turn / mdf.close
			mdf['mv'] = mdf.close*mdf.OUT_STANDING / 1000000.
			mdf.mv = mdf.mv.apply(round,0)
			dflist.append(df)
			ptlist.append(mdf)
		return dflist, ptlist
	# retrive the dataframe
	def dataSummery(self,dtime):
		masterls = self.importdata(dtime)
		ptr = masterls[0]
		ptr = masterls[['code','pt']]
		for i in range(1,len(dtime)):
			df = masterls[i][['code','pt']]
			df.columns = ['code','pt_'+ste(i)]
			ptr = merge(ptr, df, on='code')
		ptr.insert(1,'mv',ptr[dtime]['mv'])
		ptr['avg'] = ptr.apply(np.mean,axis=1)
		ptr = ptr.set_index(['code','mv'])
		ptr = ptr.sort('avg',ascending=0)
		return ptr

	def printavg(self):
		p = self.dataSummery(10)
		print p
		print p[p.iloc[:,-2] > p.iloc[:,-1]]

	def main(self):
		self.updateQOUTATION()

	def breakthrough(self,period):
		 = self.importdata(period) 



			