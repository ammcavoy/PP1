
"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""


import sys
from json import loads
from re import sub

#create .dat file object for each database
sellers_file = open('sellers.dat', 'w') # called in parseSeller()
bids_file    = open('bids.dat'   , 'w') # called in parseBids()
bidders_file = open('bidders.dat', 'w') # called in parseBidders()
items_file   = open('items.dat'  , 'w') # called in parseItems()

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        for item in items:
            #"required": ["ItemID", "Name", "Category", "Currently", "First_Bid", "Number_of_Bids", "Bids", "Location", "Country", "Started", "Ends", "Seller", "Description"]
            print(
                item['ItemId']  + 
                columnSeparator + item['UserId'] + 
                columnSeparator + item['Country'] + 
                columnSeparator + item['Location'] +
                columnSeparator + item['Name'] + 
                columnSeparator + transformDollar(item['Buy_Price']) +   #might not be in JSON
                columnSeparator + transformDollar(item['First_Bid'] + 
                columnSeparator + transformDollar(item['Currently']) + 
                columnSeparator + items['Number_of_Bids']) +
                columnSeparator + items['Description'] + 
                columnSeparator + transformDttm(items['Started'] + 
                columnSeparator + transformDttm(items['Ends']) + 
                columnSeparator + CATEGORIES!!!!!
            
            parseBids(item['Bids'], item['ItemID'])
            parseSeller(item['Seller'], item['Country'], item['Location'])
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """
            pass
        



"""
Bidder dictionary containing all the content for each bidder
    this one is correct and done - think so
"""
def parseSeller(seller, country, location):
    sys.stdout = seller_file #redirects output stream to correct dat file
    print(
        seller['UserID'] +
        columnSeparator + seller['Rating'] + 
        columnSeparator + country + 
        columnSeparator + location)
    return

"""
Bids is an array containing items
Bids{description:"Bids placed on the item", type:array, items}
    items{title:Bid, type:object, properties}
        properties{Bidder,Time,Amount}
            Bidder{description,type:object, properties, required}
                properties{Location,Country,UserID,Rating}
                    Loaction{description,type,minimum}
                    Country{description,type,minimum}
                    UserID{description, type}
                    Rating{description, type}
                required{userID, Rating}
            Time{description, type:string}
            Amount{description,type:string}
"""
def parseBids(bids, itermID):
    sys.stdout = bids_file #redirects output stream to correct dat file
    if bids is None:
        placeNullNotNone()
        return
    for bid in bids:
        print(ItemId + columnSeparator + bid['Bid']['Bidder']['UserID'] + columnSeparator + 
            transformDollar(bid['Bid']['Amount']) + columnSeparator + transformDttm(bid['bid']['Time']))
        parseBidder(bid['Bid']['Bidder'])
        # print(bids)
    return

"""
Bidder dictionary containing all the content for each bidder
"""
def parseBidder(bidder):
    sys.stdout = bidder_file #redirects output stream to correct dat file
    if bidder['Location'] is None:
        placeNullNotNone()
    if bidder['Country'] is None:
        placeNullNotNone() 
    print(bidder['UserID'] + columnSeparator + bidder['Rating']) 
    
    return

""" 
replaces "none" item fields in the JSON file with the string "NULL" 
see Loading NULL Values in the bulk-loading.pdf
"""
def placeNullNotNone():
    print("NULL")
    print(columnSeparator)
    return

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):


    if len(argv) < 2:
        print('Usage: python skeleton_json_parser.py <path to json files>', file=sys.stderr)
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print("Success parsing " + f)

if __name__ == '__main__':
    main(sys.argv)
