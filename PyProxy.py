import requests, re
from bs4 import BeautifulSoup

class PyProxy:
    def __init__(self):
        self.proxyList = []
        self.testProxyList = []
        self.proxyList.append("http://" + self.getProxy())
        self.newProxy = self.getProxy()
        
        if(self.testPopulateProxyList()== True):
            #print("Test Proxy List Populated")
             return self.populateProxyList() == True
        
    def getProxy(self):
        newProxy = self.proxyList.pop()
        return newProxy
    
    #Test Populate the proxy list with proxies from https://spys.me/proxy.txt
    def testPopulateProxyList(self):
        try:
            regex = r"[0-9]+(?:\.[0-9]+){3}:[0-9]+"
            dictHTML  = requests.get("https://spys.me/proxy.txt")
            TEST_STR = dictHTML.text
            iteratedItems = re.finditer(regex, TEST_STR, re.MULTILINE)
            with open("proxy.txt", 'w') as file:
                for iterated in iteratedItems:
                    self.testProxyList.append(iterated.group())
            return True
        except:
            return False
    
    #Populate the proxy list with proxies from https://free-proxy-list.net/
    def populateProxyList(self):
        try:
            dictHTML = requests.get("https://free-proxy-list.net/")
            soup = BeautifulSoup(dictHTML.content, "html.parser")
            parsedSoup = soup.find('textarea').get_text()
            iteratedProxyList = re.findall(regex, parsedSoup)
            with open("proxiees_list.txt", 'a') as myfile:
                for iterated in iteratedProxyList:
                    self.proxyList.append(iterated.group())
            return True
        except:
            return False 

