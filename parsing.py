from __future__ import division
from pandas import *
import numpy as np
import os
from pct_trade import qoutation as qou

class parsingClass:
	def _init__(self):
		pass
	def TRADING_TRAND(self):
		pass
	def getDATA_BASKET(self, period):
		DF_STOCK_LIST = os.listdir('df_stock/')
		dfstock = [read_csv(x,thousands=',') for x in DF_STOCK_LIST[-period]]
		dfout= read_csv('df_stock/df_main.csv')
	def getSORTED_MDF(self, df, dfout):
		mdf = merge(df, dfout)
		mdf['pc'] = mdf.SH_TRADE/ mdf.OUT_STANDING * 100
		mdf = mdf['code','name','SH_TRADE','OUT_STANDING','pc']
		SORT_MDF = mdf.sort('pc')
		return SORT_MDF
