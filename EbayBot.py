import os 
import datetime
import time
import sys
import requests
from ebaysdk.finding import Connection as finding
from ebaysdk.exception import ConnectionError

from dotenv import dotenv_values
ENV_DICTIONARY = dotenv_values('.env')
API_KEY = str(ENV_DICTIONARY['api_key'])
#API_KEY=os.getenv('api_key')

def createEbayItemString(item):
    output = ""
    try:
        if (item.title != None):
            output += "Title: " + item.title + "\n"
    except:
        pass
    try:
        if (item.itemId != None):
            output += "Item Id: " + item.itemId + "\n"
    except:
        pass
    try:
        if (item.listingInfo.listingType != None):
            output += "Listing Type: " + item.listingInfo.listingType + "\n"
    except:
        pass
    try:
        if (item.itemId.listingInfo != None):
            output += "Listing Info: " + item.listingInfo
    except:
        pass
    try:
        if (item.primaryCategory.categoryName != None):
            output += "Category Name: " + item.primaryCategory.categoryName + "\n"
    except:
        pass
    try:
        if (item.sellingStatus.currentPrice.value != None):
            output += "Current Price: " + item.sellingStatus.currentPrice.value + "\n"
    except:
        pass
    try:
        if (item.shippingInfo.shippingServiceCost != None):
            output +=  "Shipping Service Cost: " + item.shippingInfo.shippingServiceCost
    except:
        pass
    try:
        if (item.unitPrice != None):
            output += "Unit Price: " + item.unitPrice + "\n"
    except:
        pass
    try:
        if (item.listingInfo.buyItNowAvailable != None):
            output += "Buy It Now Enabled: " + item.listingInfo.buyItNowAvailable + "\n"
    except:
        pass
    try:
        if (item.listingInfo.bestOfferEnabled != None):
            output += "Best Offer Enabled: " + item.listingInfo.bestOfferEnabled + "\n"
    except:
        pass
    try:
        if (item.listingInfo.convertedBuyItNowPrice != None):
            output +=  "Buy It Now: " + item.listingInfo.convertedBuyItNowPrice
    except:
        pass
    try:
        if (item.listingInfo.endTime != None):
            output +=  "End Time: " + item.listingInfo.endTime
    except:
        pass
    try:
        if (item.sellingStatus.timeLeft != None):
            output += "Time Left: " + item.sellingStatus.timeLeft + "\n"
    except:
        pass
    try:
        if (item.sellingStatus.bidCount != None):
            output +=  "Bid Count: " + item.sellingStatus.bidCount
    except:
        pass
    try:
        if (item.sellerInfo.feedbackRattingStar != None):
            output += "FeedBack Rating: " + item.sellerInfo.feedbackRattingStar
    except:
        pass
    try:
        if (item.watchCount != None):
            output += "Watch Count: " + item.watchCount
    except:
        pass
    try:
        if (item.viewItemURL != None):
            output += "URL: " + item.viewItemURL + "\n"
    except:
        pass
    try:
        if (item.timestamp != None):
            output += "Time Stamp: " +  item.timestamp
    except:
        pass
    return output
    


class FormData(object):
    itemName = ""
    Keywords = []
    MaxPrice = 0.0
    LowPrice = 0.0
    Auction = False
    BuyNow = False
    Offer = False

class EbayBot(object):
    def __init__( self,API_KEY):
        self.api_key = API_KEY
        
#Fetch Data
    def fetchData(self):
        try:
            api = finding(appid=API_KEY, config_file=None, siteid="EBAY-US")
            response = api.execute('findItemsAdvanced', {'keywords': 'legos'})
            assert(response.reply.ack == 'Success')
            #assert(type(response.reply.timestamp) == datetime.datetime)
            #assert(type(response.reply.searchResult.item) == list)
            print(f"Total Items {response.reply.paginationOutput.totalEntries}\n")
            #item = response.reply.searchResult.item[0]
            for item in response.reply.searchResult.item:
                itemString = createEbayItemString(item)
                print(itemString)
            #assert(type(item.listingInfo.endTime) == datetime.datetime)
            #assert(type(response.dict()) == dict)

        except ConnectionError as e:
            print(e)
            print(e.response.dict())

#Parse Data
    def parseData(self):
        pass

#main      
if __name__ == '__main__':
    e = EbayBot(API_KEY)
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