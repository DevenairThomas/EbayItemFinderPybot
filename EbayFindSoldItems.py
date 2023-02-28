import requests

#SoldItemListing_BaseURL = "https://www.ebay.com/sch/i.html"

class FindSoldItems(object):
    results = []
    
    #Constructor
    def __init__(self, baseURL, headers, params):
        self.headers = headers
        self.params = params
        self.baseURL = baseURL
        
    #Setters
    def setHeaders(self, headers):
        self.headers = headers
    def setParams(self, params):
        self.params = params
    def setBaseURL(self, baseURL):
        self.baseURL = baseURL
    
    #Getters
    def getResults(self):
        results = requests.get(self.baseURL,self.headers, self.params)
        print(results.baseURL)
        return results
    def getHeaders(self):
        return self.headers
    def getParams(self):
        return self.params
    def getBaseUrl(self):
        return self.baseURL
    
EbayHeaders = """"""
{
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "referer": "https://www.ebay.com/",
    "sec-ch-ua": '"Chromium";v="89", "Google Chrome";v="89", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site"
}

EbayParams = """"""
{
    '_nkw': 'itemName',
    '_in_kw': '1',
    '_ex_kw': '',
    '_sacat': '0',
    'LH_Sold': '1',
    '_dlo': '',
    '_udlo': '',
    '_samilow': '',
    '_samihi': '',
    '_sadis': '15',
    '_sargn': '-1%26sas1c%3D1',
    'salic':'3',
    '_sop': '12',
    '_dmd': '1',
    '_ipg': '200',
    'LH_Complete': '1',
    '_forsrp':'1'
}