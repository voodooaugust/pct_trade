import os


if __name__ == '__main__':
	folders = ['qoutation','stock_dataframe','yahoodata','']
	for each in folders:
		try:
			os.stat(each)
		except:
			os.makedirs(each)