# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:02:05 2013

@author: august
"""

from __future__ import division
import urllib, re, httplib, csv, os
from HTMLParser import HTMLParser
import lxml.html
from pandas import *
from datetime import date, timedelta, datetime 

# old ccass parser, use the new one
class ccass(HTMLParser):   
    _starttag = ''
    _endtag =''
    _attr = ('','')
    _data = []
    _store = 0
    outstanding = []    
    def getCCASS_os(self,code):
        ccassurl = 'http://www.hkexnews.hk/sdw/search/search_sdw.asp'  
        para = {\
        'txt_today_d':'1',\
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
        content = urllib.urlopen(ccassurl,value).read()
        return content
    def handle_starttag(self,tag,attr):
        self._starttag = getattr(object,  name, default)
        self._attr = attr
    def handle_endtag(self,tag):
        self._endtag = tag
    def handle_data(self,data):
        if self._starttag == 'table':
            self._store += 1
        elif self._endtag == 'table':
            self._store -= 1
        if  self._store == 4 :
            self._data.append(data)            
    def getdata(self):
        return self._data        
    def lxmlstringparser(self,datastring):
        try:
            htmltree = lxml.html.fromstring(datastring)
            factsheet = htmltree.xpath('//table[@bordercolor="blue"]//td//text()')
            return factsheet
        finally:
            return ''              
    def dataCleaning(self,data):
        try:
            ls = [x.replace('\xa0','') for x in data]
            ls = [str(x) for x in ls if re.match('[\w\d\,]',x)]
            return ls    
        finally:
            pass
    def getOS(self,code):
        for x in code:
            try:
                raw = self.getCCASS_os(x)
            finally:
                pass
            factlist = self.dataCleaning(self.lxmlStringParser(raw))
            self.outstanding.append(factlist[-1])
    def getOutstanding(self):
        return self.outstanding
        

class htmlcleaner(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self,data):
        self.fed.append(data)
    def getdata(self):
        return ''.join(self.fed)


class qoutation:
    def __init__(self):
        self.folderpath = 'qoutations\\'
        self.df_stock = 'stock_dataframe\\'
        self.filelist = os.listdir(self.folderpath)
        self.dflist = os.listdir(self.df_stock)
    '''
    def retriMajorStockList(self):
        self.md = self.downloadqout()
        self.ls =self.parseQoutation(self.md)
        with open('majorstocklist.txt','w') as f:
            for item in self.ls:
                f.write('%s\n' % item[0])
            f.close()
    '''
    def downloadqout(self,timerange):
        print 'begining download qouation from hkex'
        date = self.setDate(timerange)
        baseurl = r'http://www.hkex.com.hk/eng/stat/smstat/dayquot/d'
        for eachdate in date:
            print ' ------ downloading qoutation date : %s' % eachdate
            url = baseurl + eachdate + 'e.htm'
            urllib.urlretrieve(url,self.folderpath+'q'+eachdate+'.txt')
        print 'finish download the quatation files \n\nwith timerange %s\
        \n\nexit from procedure dowloadqout' % timerange
    # parseqoutation and output to the df_stock folder with DataFrame dtype
    '''
    def parseQoutation(self,massdata,datecode):
        try:
            starting_word = r' +1.+?HKD'
            ending_word = r' +6898.+?HKD'
            s_pt = re.search(starting_word,massdata).start()
            e_pt = re.search(ending_word,massdata).end() + 123
            data =  massdata[s_pt:e_pt]
            mc = htmlcleaner()
            mc.feed(data)
            data = mc.getdata()
            pat = r' +(\d+) (.+) (HKD) +([\d|\.]+) +([\d|\.]+) +([\d|\.]+) +([\d|\,]+)\n +([\d|\.]+) +([\d|\.]+) +([\d|\.]+) +([\d|\,]+)'
            ls = re.findall(pat,data)
            return ls
        finally:
            print 'finish parseQoutation with datecode : %s' % datecode
    
    def tocsvfile(self,ls,datecode):
        print 'putting the file to stock_dataframe : %s' % datecode
        colname = ['code','name','cur','pclose','ask','high','SH_TRADE','close','bid','low','turn']
        df = DataFrame(ls,columns=colname)
        df.to_csv('stock_dataframe\\df_'+ datecode +'.txt',index = 0)
    '''
    def setDate(self,daterange):
        today = date.today()
        datelist = []
        for x in range(daterange):
            day = today - timedelta(x+1)
            if day.weekday() not in [5,6]:
                datelist.append(day.strftime('%y%m%d'))
                print day.strftime('%y%m%d')
        return datelist
    def returnDays(self):
        today = datetime.today()
        lastfile = os.listdir(self.folderpath)
        print 'number of files in qoutation %s' % len(lastfile)
        if lastfile:
            lf =  lastfile[-1]
            print 'the date of today %s, and the name of lastfile %s' % (today, lf)
            rawdate = lf.strip('q.txt')
            d = datetime.strptime(rawdate,'%y%m%d')
            days = (today - d).days
            return days
        else:
            return 9
    def stocklist(self):
        print 'get the stocklist from majorstocklist.txt'
        with open('majorstocklist.txt','rb') as f:
            csvread = csv.reader(f)
            ls = []
            for x in csvread:
                ls = ls + x
            f.close()
            self.sl = ls
            return ls
    # the old dataframe construction to the from folder qoutation
    '''
    def constructDataFrame(self):
        filelist = os.listdir(self.folderpath)
        for each in filelist:
            print 'begining to constructing dataframe : %s' % each
            filename = self.folderpath + each
            with open(filename) as f:
                con = f.read()
                if len(con) > 10000:
                    datecode = each.strip('q.txt')
                    self.parseQoutation(con,datecode)
                f.close()
    def dataframeqoutation(self):
        self.df = []
        for each in self.dflist:
            print 'begining running dataframeqoutation : %s' % each
            eachfile = self.df_stock + each
            self.df.append(read_csv(eachfile,thousands=',',index_col=0))
    def dispdf(self):
        for each in self.df:
            each['pct'] = each.trade/each.ss
            e = each.sort('pct',ascending=0)
            print e[:10]
    '''
    def updateDataFrame(self,t):
        filelist = os.listdir(self.folderpath)
        lastfile = filelist[-t:]
        if t == 0:
            pass
        else:
            for each in lastfile:
                print 'processing the dataframe : %s ' % each
                filename = self.folderpath + each
                if os.path.getsize(filename) > 5000:
                    datecode = each.strip('q.txt')
                    f = open(filename)
                    ls = self.returnDATA(f.read(),datecode)
                    ls.to_csv('stock_dataframe\\df_'+ datecode +'.txt',index = 0)
                    f.close()
    def updateQoutation(self):
        t = self.returnDays()
        if t == 0:
            t = 1
        self.updateAll(t)
    def updateAll(self,t):
        self.downloadqout(t)
        self.updateDataFrame(t)        
        print 'finish updateall qoutation with days: %s' % t


    def returnDATA(self,rawdata, datecode):
        pat2 = ' +(\\d+) (.+) (HKD) +([\\d|\\.|-]+) +([\\d|\\.|-]+) +([\\d|\\.|-]+) +([\\d|\\,|-]+)\n +([\\d|\\.|-]+) +([\\d|\\.|-]+) +([\\d|\\.|-]+) +([\\d|\\,|-]+)'
        fr = DataFrame(re.findall(pat2,rawdata))
        fr.replace(r'-','0',inplace=True)
        fr[fr.columns[3:]] = fr.ix[:,3:].applymap(lambda x:x.replace(',','')).astype(float)
        colname = ['code','name','cur','pclose','ask','high','SH_TRADE','close','bid','low','turn']
        fr.columns = colname
        print 'finish returnDATA with datecode : %s' % datecode
        return fr
#  update/get days diff > downloadqout > parseQoutation > tocsvfile
# 
# 
# 
# 
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
