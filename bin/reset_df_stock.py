from pandas import *
import os

filepath = 'df_stock/'
colname = ['code','name','cur','pclose','ask','high','SH_TRADE','close','bid','low','turn']
for each in os.listdir(filepath):
	datafile = filepath + each
	df = read_csv(datafile)
	df.columns = colname
	df.to_csv('stock_dataframe/'+each,index=0)
