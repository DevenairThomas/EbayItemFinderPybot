

class SearchFilterItem(object):
    def __init__(self):
        pass
    
    #Dictionary of all the filter options
    FilterDict = {}
    
    #List ItemFilter
    ItemFilter = []
    
    #List PaginationInput
    PaginationInput = []
    
    #Filter options
    ItemName = ""
    Keywords = []
    MaxPrice = ""
    MinPrice = ""
    Condition = ""
    Currency = ""
    MaxBids = ""
    AvailableTo = ""
    FeedbackScoreMin = ""
    FeedbackScoreMax = ""
    EndTimeFrom = ""
    EndTimeTo = ""
    ListedIn = ""
    LocatedIn = ""
    EntriesPerPage = ""
    PageNumber = ""
    ExpeditedShippingType = ""
    ListingType = ""
    MaxDistance = ""
    MaxHandlingTime = ""
    MaxQuantity = ""
    MinBids = ""
    MinQuantity = ""
    ModTimeFrom = ""
    PaymentMethod = ""
    Seller = ""
    SellerBusinessType = ""
    LocalSearchOnly = False
    LocalPickupOnly = False
    HideDuplicateItems = False
    GetItFastOnly = False
    FreeShippingOnly = False
    ExcludeSeller = ""
    ExcludeCategory = False
    ExcludeAutoPay = False
    CharityOnly = False
    BestOfferOnly = False
    Auction = False
    BuyNow = False
    Offer = False  
    LotsOnly = False  
    ReturnsAcceptedOnly = False  
    TopRatedSellerOnly = False
    ValueBoxInventory = False
    BuyItNowOnly = False

    #Dictionary of all the filter options
    def createSearchFilterDict(self):
        self.FilterDict["Keywords"] = self.ItemName + ", "
        for words in self.Keywords:
            self.FilterDict["Keywords"] += words + ", "
        self.FilterDict["MaxPrice"] = self.MaxPrice
        self.FilterDict["MinPrice"] = self.LowPrice
        self.FilterDict["Condition"] = self.Condition
        self.FilterDict["Currency"] = self.Currency
        self.FilterDict["MaxBids"] = self.MaxBids
        self.FilterDict["AvailableTo"] = self.AvailableTo
        self.FilterDict["FeedbackScoreMin"] = self.FeedbackScoreMin
        self.FilterDict["FeedbackScoreMax"] = self.FeedbackScoreMax
        self.FilterDict["EndTimeFrom"] = self.EndTimeFrom
        self.FilterDict["EndTimeTo"] = self.EndTimeTo
        self.FilterDict["ListedIn"] = self.ListedIn
        self.FilterDict["LocatedIn"] = self.LocatedIn
        self.FilterDict["EntriesPerPage"] = self.EntriesPerPage
        self.FilterDict["PageNumber"] = self.PageNumber
        self.FilterDict["ExpeditedShippingType"] = self.ExpeditedShippingType
        self.FilterDict["ListingType"] = self.ListingType
        self.FilterDict["MaxDistance"] = self.MaxDistance
        self.FilterDict["MaxHandlingTime"] = self.MaxHandlingTime
        self.FilterDict["MaxQuantity"] = self.MaxQuantity
        self.FilterDict["MinBids"] = self.MinBids
        self.FilterDict["MinQuantity"] = self.MinQuantity
        self.FilterDict["ModTimeFrom"] = self.ModTimeFrom
        self.FilterDict["PaymentMethod"] = self.PaymentMethod
        self.FilterDict["Seller"] = self.Seller
        self.FilterDict["SellerBusinessType"] = self.SellerBusinessType
        self.FilterDict["LocalSearchOnly"] = self.LocalSearchOnly
        self.FilterDict["LocalPickupOnly"] = self.LocalPickupOnly
        self.FilterDict["HideDuplicateItems"] = self.HideDuplicateItems
        self.FilterDict["GetItFastOnly"] = self.GetItFastOnly
        self.FilterDict["FreeShippingOnly"] = self.FreeShippingOnly
        self.FilterDict["ExcludeSeller"] = self.ExcludeSeller
        self.FilterDict["ExcludeCategory"] = self.ExcludeCategory
        self.FilterDict["ExcludeAutoPay"] = self.ExcludeAutoPay
        self.FilterDict["CharityOnly"] = self.CharityOnly
        self.FilterDict["BestOfferOnly"] = self.BestOfferOnly
        self.FilterDict["Auction"] = self.Auction
        self.FilterDict["BuyNow"] = self.BuyNow
        self.FilterDict["Offer"] = self.Offer
        self.FilterDict["LotsOnly"] = self.LotsOnly
        self.FilterDict["ReturnsAcceptedOnly"] = self.ReturnsAcceptedOnly
        self.FilterDict["TopRatedSellerOnly"] = self.TopRatedSellerOnly
        self.FilterDict["ValueBoxInventory"] = self.ValueBoxInventory
        self.FilterDict["ExpeditedShippingType"] = self.ExpeditedShippingType
        self.FilterDict["BuyItNowOnly"] = self.BuyItNowOnly
    
    #TODO: Create a function that will return the api call
    def getApiExecute(self):
        pass
        
    def getKeyWords(self):
        try:
            if(self.FormDataObject.itemName != ""):
                return self.FormDataObject.itemName
        except:
            pass
        
    def getMaxPrice(self):
        try:
            if(self.FormDataObject.MaxPrice != ""):
                return {'name': 'MaxPrice','value': float(self.FormDataObject.MaxPrice), 'paramName': 'Currency', 'paramValue': self.FormDataObject.Currency}
        except:
            pass
        
    def getMinPrice(self):
        try:
            if(self.FormDataObject.MinPrice != ""):
                return {'name': 'MinPrice','value': float(self.FormDataObject.MinPrice), 'paramName': 'Currency', 'paramValue': self.FormDataObject.Currency}
        except:
            pass
    def getCondition(self):
        try:
            if(self.FormDataObject.Condition != ""):
                return {'name': 'Condition','value': self.FormDataObject.Condition}
        except:
            pass
    def getCurrency(self):
        try:
            if(self.FormDataObject.Currency != ""):
                return {'name': 'Currency','value': self.FormDataObject.Currency}
        except:
            pass
    def getMaxBids(self):
        try:
            if(self.FormDataObject.MaxBids != ""):
                return {'name': 'MaxBids','value': int(self.FormDataObject.MaxBids)}
        except:
            pass
    def getAvailableTo(self):
        try:
            if(self.FormDataObject.AvailableTo != ""):
                return {'name': 'AvailableTo','value': self.FormDataObject.AvailableTo}
        except:
            pass
    def getFeedbackScoreMin(self):
        try:
            if(self.FormDataObject.FeedbackScoreMin != ""):
                return {'name': 'FeedbackScoreMin','value': int(self.FormDataObject.FeedbackScoreMin)}
        except:
            pass
    def getFeedbackScoreMax(self):
        try:
            if(self.FormDataObject.FeedbackScoreMax != ""):
                return {'name': 'FeedbackScoreMax','value': int(self.FormDataObject.FeedbackScoreMax)}
        except:
            pass
    #Have to pass all times in GMT
    def getEndTimeFrom(self):
        try:
            if(self.FormDataObject.EndTimeFrom != ""):
                return {'name': 'EndTimeFrom','value': self.FormDataObject.EndTimeFrom}
        except:
            pass
    def getEndTimeTo(self):
        try:
            if(self.FormDataObject.EndTimeTo != ""):
                return {'name': 'EndTimeTo','value': self.FormDataObject.EndTimeTo}
        except:
            pass
    def getListedIn(self):
        try:
            if(self.FormDataObject.ListedIn != ""):
                return {'name': 'ListedIn','value': self.FormDataObject.ListedIn}
        except:
            pass
    def getLocatedIn(self):
        try:
            if(self.FormDataObject.LocatedIn != ""):
                return {'name': 'LocatedIn','value': self.FormDataObject.LocatedIn}
        except:
            pass
    #Might Work
    def getEntriesPerPage(self):
        try:
            if(self.FormDataObject.EntriesPerPage != ""):
                return {'entriesPerPage', self.FormDataObject.EntriesPerPage}
        except:
            pass
    def getPageNumber(self):
        try:
            if(self.FormDataObject.PageNumber != ""):
                return {'pageNumber': self.FormDataObject.PageNumber}
        except:
            pass
    def getExpeditedShippingType(self):
        try:
            if(self.FormDataObject.ExpeditedShippingType != ""):
                return {'name': 'ExpeditedShippingType','value': self.FormDataObject.ExpeditedShippingType}
        except:
            pass
    def getListingType(self):
        try:
            if(self.FormDataObject.ListingType != ""):
                return {'name': 'ListingType','value': self.FormDataObject.ListingType}
        except:
            pass
    def getMaxDistance(self):
        try:
            if(self.FormDataObject.MaxDistance != ""):
                return {'name': 'MaxDistance','value': self.FormDataObject.MaxDistance}
        except:
            pass
    def getMinBids(self):
        try:
            if(self.FormDataObject.MinBids != ""):
                return {'name': 'MinBids','value': self.FormDataObject.MinBids}
        except:
            pass
    def getModTimeFrom(self):
        try:
            if(self.FormDataObject.ModTimeFrom != ""):
                return {'name': 'ModTimeFrom','value': self.FormDataObject.ModTimeFrom}
        except:
            pass
    def getModTimeTo(self):
        try:
            if(self.FormDataObject.ModTimeTo != ""):
                return {'name': 'ModTimeTo','value': self.FormDataObject.ModTimeTo}
        except:
            pass
    def getPaymentMethod(self):
        try:
            if(self.FormDataObject.PaymentMethod != ""):
                return {'name': 'paymentMethod','value': self.FormDataObject.PaymentMethod}
        except:
            pass
    def getReturnsAcceptedOnly(self):
        try:
            if(self.FormDataObject.ReturnsAcceptedOnly != False):
                return {'name': 'ReturnsAcceptedOnly','value': self.FormDataObject.ReturnsAcceptedOnly}
        except:
            pass
    def getSafeSearch(self):
        try:
            if(self.FormDataObject.SafeSearch != False):
                return {'name': 'SafeSearch','value': self.FormDataObject.SafeSearch}
        except:
            pass
    def getTopRatedSellerOnly(self):
        try:
            if(self.FormDataObject.TopRatedSellerOnly != False):
                return {'name': 'TopRatedSellerOnly','value': self.FormDataObject.TopRatedSellerOnly}
        except:
            pass
    def getFreeShippingOnly(self):
        try:
            if(self.FormDataObject.FreeShippingOnly != False):
                return {'name': 'FreeShippingOnly','value': self.FormDataObject.FreeShippingOnly}
        except:
            pass
    def getHideDuplicateItems(self):
        try:
            if(self.FormDataObject.HideDuplicateItems != False):
                return {'name': 'HideDuplicateItems','value': self.FormDataObject.HideDuplicateItems}
        except:
            pass
    def getSoldItemsOnly(self):
        try:
            if(self.FormDataObject.SoldItemsOnly != False):
                return {'name': 'SoldItemsOnly','value': self.FormDataObject.SoldItemsOnly}
        except:
            pass
    def getFeaturedOnly(self):
        try:
            if(self.FormDataObject.FeaturedOnly != False):
                return {'name': 'FeaturedOnly','value': self.FormDataObject.FeaturedOnly}
        except:
            pass
    def getLocalPickupOnly(self):
        try:
            if(self.FormDataObject.LocalPickupOnly != False):
                return {'name': 'LocalPickupOnly','value': self.FormDataObject.LocalPickupOnly}
        except:
            pass
    def getLocalSearchOnly(self):
        try:
            if(self.FormDataObject.LocalSearchOnly != False):
                return {'name': 'LocalSearchOnly','value': self.FormDataObject.LocalSearchOnly}
        except:
            pass
    def getWorldOfGoodOnly(self):
        try:
            if(self.FormDataObject.WorldOfGoodOnly != False):
                return {'name': 'WorldOfGoodOnly','value': self.FormDataObject.WorldOfGoodOnly}
        except:
            pass
    def getCharityOnly(self):
        try:
            if(self.FormDataObject.CharityOnly != False):
                return {'name': 'CharityOnly','value': self.FormDataObject.CharityOnly}
        except:
            pass
    def getAuctionItemsOnly(self):
        try:
            if(self.FormDataObject.AuctionItemsOnly != False):
                return {'name': 'AuctionItemsOnly','value': self.FormDataObject.AuctionItemsOnly}
        except:
            pass
    def getBestOfferOnly(self):
        try:
            if(self.FormDataObject.BestOfferOnly != False):
                return {'name': 'BestOfferOnly','value': self.FormDataObject.BestOfferOnly}
        except:
            pass
    def getValueBoxInventory(self):
        try:
            if(self.FormDataObject.ValueBoxInventory != False):
                return {'name': 'ValueBoxInventory','value': self.FormDataObject.ValueBoxInventory}
        except:
            pass
    def getExcludeSeller(self):
        try:
            if(self.FormDataObject.ExcludeSeller != ""):
                return {'name': 'ExcludeSeller','value': self.FormDataObject.ExcludeSeller}
        except:
            pass
    def getLotsOnly(self):
        try:
            if(self.FormDataObject.LotsOnly != False):
                return {'name': 'LotsOnly','value': self.FormDataObject.LotsOnly}
        except:
            pass
    def getBuyItNowOnly(self):
        try:
            if(self.FormDataObject.BuyItNowOnly != False):
                return {'name': 'BuyItNowOnly','value': self.FormDataObject.BuyItNowOnly}
        except:
            pass
        
    #return the item filter
    def setItemFilter(self):
        self.ItemFilter += self.getKeyWords()
        self.ItemFilter += self.getBuyItNowOnly()
        self.ItemFilter += self.getEndTimeFrom()
        self.ItemFilter += self.getEndTimeTo()
        self.ItemFilter += self.getExpeditedShippingType()
        self.ItemFilter += self.getFeaturedOnly()
        self.ItemFilter += self.getFreeShippingOnly()
        self.ItemFilter += self.getHideDuplicateItems()
        self.ItemFilter += self.getListingType()
        self.ItemFilter += self.getLocalPickupOnly()
        self.ItemFilter += self.getLocalSearchOnly()
        self.ItemFilter += self.getMaxDistance()
        self.ItemFilter += self.getMinBids()
        self.ItemFilter += self.getModTimeFrom()
        self.ItemFilter += self.getModTimeTo()
        self.ItemFilter += self.getPaymentMethod()
        self.ItemFilter += self.getReturnsAcceptedOnly()
        self.ItemFilter += self.getSafeSearch()
        self.ItemFilter += self.getTopRatedSellerOnly()
        self.ItemFilter += self.getMaxPrice()
        self.ItemFilter += self.getMinPrice()
        self.ItemFilter += self.getSoldItemsOnly()
        self.ItemFilter += self.getWorldOfGoodOnly()
        self.ItemFilter += self.getCharityOnly()
        self.ItemFilter += self.getCondition()
        self.ItemFilter += self.getValueBoxInventory()
        self.ItemFilter += self.getExcludeSeller()
        self.ItemFilter += self.getLotsOnly()
        self.ItemFilter += self.getAuctionItemsOnly()
        self.ItemFilter += self.getBestOfferOnly()
        self.ItemFilter += self.getLocatedIn()
        self.ItemFilter += self.getListedIn()
        self.ItemFilter += self.getFeedbackScoreMax()
        self.ItemFilter += self.getFeedbackScoreMin()
        self.ItemFilter += self.getAvailableTo()
        self.ItemFilter += self.getMaxBids()
        
    def setPaginationInput(self):
        self.PaginationInput += self.getPageNumber()
        self.PaginationInput += self.getEntriesPerPage()