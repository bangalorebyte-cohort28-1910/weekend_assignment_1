import requests
import json

class Markit:
	def __init__(self):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json"

	def company_search(self,string):
		url=self.lookup_url+'?input='+string
		urlSource=requests.get(url,timeout=2)
		if urlSource.status_code==200:
			companyDetails=json.loads(urlSource.text)
			if companyDetails!=[]:
				symbol=companyDetails[0]['Symbol']
				return symbol
		return 'Fail'
	
	def get_quote(self,string):
		url=self.quote_url+'?symbol='+string
		urlSource=requests.get(url,timeout=2)
		if urlSource.status_code==200:
			stockInfo=json.loads(urlSource.text)
			currentPrice=stockInfo['LastPrice']
			return currentPrice
		return 'Fail'


def GetCompany(stockName):
	company=Markit()
	return company.company_search(stockName)

def GetCurrentPrice(stockSymbol):
	company=Markit()
	return company.get_quote(stockSymbol)

