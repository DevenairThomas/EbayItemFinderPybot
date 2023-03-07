import os 
import datetime
import time
import sys
import requests
from ebaysdk.finding import Connection as finding
from ebaysdk.exception import ConnectionError
from dotenv import dotenv_values
import ResponseOutputData
import SearchFilterItem

#retrieve api key from .env file
ENV_DICTIONARY = dotenv_values('.env')
#retrieve api key from environment variable
API_KEY = str(ENV_DICTIONARY['api_key'])
#API_KEY=os.getenv('api_key')

SearchFilter = SearchFilterItem
ResponseData = ResponseOutputData

#Class that fetches and parses data from ebay
class EbayFinderBot(object):
    AllItemDict = {}
    #TODO: Get file path from user
    FilerDestination = "C:\\Users\\joshu\\Desktop\\EbayF"
    
    def __init__( self,API_KEY,SearchFilterData):
        self.api_key = API_KEY
        self.SearchFilterData = SearchFilterData
        
#Fetch Finding Item Data
    def fetchData(self,SearchFilterData):
        try:
            api = finding(appid=API_KEY, config_file=None, siteid="EBAY-US")
            
            response = api.execute(
                'findItemsAdvanced',
                {'keywords': self.FormDataObject.itemName, """"""
                'itemFilter': [{'name': 'MaxPrice', 'value': self.FormDataObject.MaxPrice,'paramName': 'Currency', 'paramValue': 'USD'}, {'name': 'ListingType', 'value': 'AuctionWithBIN'}], 
                'paginationInput': {'entriesPerPage': '100', 'pageNumber': '1'}})
            
            assert(response.reply.ack == 'Success')
            #assert(type(response.reply.timestamp) == datetime.datetime)
            #assert(type(response.reply.searchResult.item) == list)
            
            print(f"Total Items {response.reply.paginationOutput.totalEntries}\n")
            
            #item = response.reply.searchResult.item[0]
            
            for item in response.reply.searchResult.item:
                ResponseData.createEbayOutputString( self.FormDataObject.itemName, item)
                #print(itemString)

            #assert(type(item.listingInfo.endTime) == datetime.datetime)
            #assert(type(response.dict()) == dict)

        except ConnectionError as e:
            print(e)
            print(e.response.dict())
          
    def findItemsAdvanced(self, api, FormData, paginationInput):
        #response = api.execute('findItemsAdvanced',{'keywords': self.FormDataObject.itemName, 'itemFilter': [{'name': 'MaxPrice', 'value': self.FormDataObject.MaxPrice, 'paramName': 'Currency', 'paramValue': 'USD'}, {'name': 'ListingType', 'value': 'AuctionWithBIN'}], 'paginationInput': {'entriesPerPage': '100', 'pageNumber': '1'}})
        tempFormData = FormData
        

#Parse Data, Write to file
    def parseData(self):
        pass

#main      
if __name__ == '__main__':
    e = EbayFinderBot(API_KEY)
    e.fetchData()
    e.parseData()
    
#if __name__ == '__main__':
#    if len(sys.argv) < 2:
#        print("need s or c as argument")
#    elif sys.argv[1] == "s":
#        pipe_server()
#    elif sys.argv[1] == "c":
#        pipe_client()
#    else:
#        print(f"no can do: {sys.argv[1]}")