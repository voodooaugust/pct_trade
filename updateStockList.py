from pandas import *
import os, re, lxml

class stocklist():
	def __init__(self):
		self.dfpath = 'stock_dataframe/'
		self.filelist = os.listdir(self.dfpath)

	def updatelist(self):
		lf = self.filelist[-1]
		df = read_csv(ls,thousands=',')
		codels = df.code
		for each in codels.iterrows()
			self.updateProc(each)
	def updateProc(self,name):
		pass



# 
class share_out:
    def updateShare(self, stockcode):
        ptr = stockcode.index(0)
        sc = stockcode[ptr:]
        for c in sc:
            code = str(c)
            print ' now processing '+ code 
            ccassurl = 'http://www.hkexnews.hk/sdw/search/search_sdw.asp'  
            para = {'txt_today_d':'1',\
            'txt_today_m':'4',\
            'txt_today_y':'2013',\
            'current_page':'1',\
            'stock_market':'HKEX',\
            'IsExist_Slt_Stock_Id':'False',\
            'IsExist_Slt_Part_Id':'False',\
            'rdo_SelectSortBy':'Shareholding',\
            'sel_ShareholdingDate_d':'29',\
            'sel_ShareholdingDate_m':'03',\
            'sel_ShareholdingDate_y':'2013',\
            'txt_stock_code':code,\
            'txt_stock_name':'',\
            'txt_ParticipantID':'',\
            'txt_Participant_name':''}
            value = urllib.urlencode(para)
            con = urllib.urlopen(ccassurl,value)
            print con.getcode()
            if con.getcode() == 200:
                content = con.read()
                filename = code + '.txt'
                self.write2file(content,filename)
            print ' ----------------------' + str(ptr)
            ptr += 1
            con.close()
            # headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html"}
            # connect =  httplib.HTTPConnection(ccassurl)
            # connect.request("POST",'',value,headers)
            # res = connect.getresponse()
            # connect.close()
            # print res.status
            # filename = code + '.txt'
            # self.write2file(content,filename)
    def write2file(self,content,filename):
        with open(filename,'w') as f:
            f.write(content)
            f.close()
    def stocklist(self):
        with open('majorstocklist.txt','rb') as f:
            csvread = csv.reader(f)
            ls = []
            for x in csvread:
                ls = ls + x
            f.close()
            self.sl = ls
            return ls
    def getOutstandingShares(self):
        os_list = []
        error_list = []
        for x in self.stocklist():
            filename = x + '.txt'
            with open(filename) as f:
                con = f.read()
                Out_share = self.lxmlstringparser(con)
                print '-----------'
                print 'now processing ' + filename
                if Out_share:
                    print Out_share[-1]
                    os_list.append((x,Out_share[-1]))
                else:
                    error_list += x                
                f.close()
        print os_list
        with open('outstanding_share.txt','w') as f:
            cw = csv.writer(f)
            for row in os_list:
                cw.writerow(row)
            f.close()
        with open('error.txt','w') as f:
            cw = csv.writer(f)
            for row in error_list:
                cw.writerow(row)
            f.close()
    def lxmlstringparser(self,datastring,stockcode):
        htmltree = lxml.html.fromstring(datastring)
        factsheet = htmltree.xpath('//table[@bordercolor="blue"]//td//text()')
        factsheet = [x.replace(',','') for x in factsheet if re.match('[^/|\xa0|\r]',x)] 
        if len(factsheet) > 1: 
            result = [stockcode, factsheet[-1]]
            return result 
    def dfSTOCKLIST(self):
        filepath = 'stock_dataframe\\'
        temp = os.getcwd()
        os.chdir(filepath)
        ls = os.listdir(os.getcwd())
        df = read_csv(ls[-1],thousands=',')
        os.chdir(temp)
        return list(df.code )
    def getOSS(self):
        error_list = []
        datalist = []
        ls = self.stock_list
        for each in ls:
            x = str(each)
            filename = 'outstanding\\'+x + '.txt'
            with open(filename) as f:
                con = f.read()
                Out_share = self.lxmlstringparser(con,x)
                print '-----------'
                print 'now processing ' + filename
                if Out_share:
                    print Out_share[-1]
                    datalist.append(Out_share)
                else:
                    error_list.append(x)                
                f.close()
        df = DataFrame(datalist)
        df.columns = ['no','code','OUT_STAND']
        df.to_csv('df_main.csv')
        DataFrame(error_list).to_csv('error.csv')
    def __init__(self):
        self.stock_list = self.dfSTOCKLIST()
        self.DATAFRAME_DESTINATION = 'df_outstanding\\'
