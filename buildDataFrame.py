import os, re
from HTMLParser import HTMLParser
from pandas import *
class htmlcleaner(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	def handle_data(self,data):
		self.fed.append(data)
	def getdata(self):
		return ''.join(self.fed)


class buildDataFrame():
	def __init__(self):
		self.qFolder = 'qoutations/'
	def parseQoutation(self,massdata,datecode):
		starting_word = r' +1 CHEUNG KONG      HKD'
		ending_word = r' +6889 DYNAM JAPAN      HKD'
		s_pt = re.search(starting_word,massdata).start()
		e_pt = re.search(ending_word,massdata).end() + 123
		data =  massdata[s_pt:e_pt]
		mc = htmlcleaner()
		mc.feed(data)
		data = mc.getdata()
		pat = r' +(\d+) (.+) (HKD) +([\d|\.]+) +([\d|\.]+) +([\d|\.]+) +([\d|\,]+)\n +([\d|\.]+) +([\d|\.]+) +([\d|\.]+) +([\d|\,]+)'
		ls = re.findall(pat,data)
		return ls
	def build(self):
		flist = os.listdir(self.qFolder)
		print 'Build all the dataframe !'
		for each in flist:
			filename = self.qFolder + each
			if os.path.getsize(filename) > 5000:
				datecode = each.strip('q.txt')
				f = open(filename)
				ls = self.parseQoutation(f.read(),datecode)
				self.tocsvfile(ls,datecode)
				f.close()
	def tocsvfile(self,ls,datecode):
		print 'putting the file to stock_dataframe : %s' % datecode
		colname = ['code','name','cur','pclose','ask','high','SH_TRADE','close','bid','low','turn']
		df = DataFrame(ls,columns=colname)
		df.to_csv('stock_dataframe\\df_'+ datecode +'.txt',index = 0)
