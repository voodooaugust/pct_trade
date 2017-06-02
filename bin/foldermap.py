import os

def create_directory():
	folders = set(['qoutations','stock_dataframe'])
	wd = set(os.listdir(os.getcwd()))
	missing = (folders | wd) - wd
	print 'the missing folders is '
	print  list(missing)
	for each in list(missing):
		os.makedirs(each)
create_directory()