
"""
FILE: skeleton_parser2.py
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

# create .dat file object for each database
#sellers_file = open('sellers.dat', 'w')  # called in parseSeller()
bids_file = open('bids.dat', 'w')  # called in parseBids()
#bidders_file = open('bidders.dat', 'w')  # called in parseBidders()
items_file = open('items.dat', 'w')  # called in parseItems()
users_file = open('users.dat', 'w') # called by parseSellers() and parsebidders()
categories_file = open('categories.dat', 'w')

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
        'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

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
        # creates a Python dictionary of Items for the supplied json file
        items = loads(f.read())['Items']
        for item in items:
            # "required": ["ItemID", "Name", "Category", "Currently", "First_Bid", "Number_of_Bids", "Bids", "Location", "Country", "Started", "Ends", "Seller", "Description"]
            sys.stdout = items_file  # redirects output stream to correct dat file
            print(
                item['ItemID'] +
                columnSeparator + sqlString(item['Seller']['UserID']) +
                columnSeparator + sqlString(item['Country']) +
                columnSeparator + sqlString(item['Location']) +
                columnSeparator + sqlString(item['Name']), end='')
                # columnSeparator + transformDollar(item['Buy_Price']) +   #might not be in JSON
            if 'Buy_Price' in item.keys():
                print(columnSeparator +
                      transformDollar(item['Buy_Price']), end='')
            else:
                print(columnSeparator + "\"NULL\"", end='')
            
            print(
                columnSeparator + transformDollar(item['First_Bid']) +
                columnSeparator + transformDollar(item['Currently']) +
                columnSeparator + item['Number_of_Bids'] +
                columnSeparator + transformDollar(item['Started']) + 
                columnSeparator + transformDttm(item['Ends']), end = '')
                
            if item['Description'] == None or len(item['Description']) == 0:
                print(columnSeparator + "\"NULL\"")
            else:
                print(columnSeparator + sqlString(item['Description']))    


            """
            print(columnSeparator + "\"||", end='') # begin Categories string
            for category in item['Category']:
                print(category + '|', end = '')
            print("|\"") ## end Categories 
            """
            numcat = parseCategories(item['Category'], item['ItemID'])
            # sys.stdout = items_file  # redirects output stream to correct dat file
            # print(columnSeparator + numcat)
            parseBids(item['Bids'], item['ItemID'])
            parseSeller(item['Seller'], item['Country'], item['Location'])
            
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """
            pass


def parseCategories(categories, itemID):
    sys.stdout = categories_file #redirects output stream to correct dat file
    numCategories = 0
    for category in categories:
        numCategories +=1
        print(
            itemID + 
            columnSeparator + sqlString(category)
        )
    return numCategories


"""
Bidder dictionary containing all the content for each bidder
    this one is correct and done - think so
"""
def parseSeller(seller, country, location):
    sys.stdout = users_file #redirects output stream to correct dat file
    print(
        sqlString(seller['UserID']) + 
        columnSeparator + seller['Rating'] + 
        columnSeparator + sqlString(country) +
        columnSeparator + sqlString(location))
    return

"""
Bids is an array containing items
Bid description below:
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
def parseBids(bids, ItemID):
    sys.stdout = bids_file #redirects output stream to correct dat file
    if bids is None:
        # i think this should be commented out, and just return with no prints - adam
        # placeNullNotNone()  # this will give us a single line in the bids file that just has "NULL|" is this what we want????
        return
    for bid in bids:
        sys.stdout = bids_file #redirects output stream to correct dat file
        print(sqlString(bid['Bid']['Bidder']['UserID']) + columnSeparator + sqlString(ItemID) + columnSeparator + 
            transformDollar(bid['Bid']['Amount']) + columnSeparator + transformDttm(bid['Bid']['Time']))
        parseBidder(bid['Bid']['Bidder'])
    return

"""
Bidder dictionary containing all the content for each bidder
"""
def parseBidder(bidder):
    sys.stdout = users_file #redirects output stream to correct dat file 
    
    print(
        sqlString(bidder['UserID']) +
        columnSeparator + bidder['Rating'], end = '') 
    if 'Country' in bidder.keys():
        print(columnSeparator + sqlString(bidder['Country']), end = '')
    else:
        print(columnSeparator + "\"NULL\"", end = '')
    if 'Location' in bidder.keys():
        print(columnSeparator + sqlString(bidder['Location']))
    else:
        print(columnSeparator + "\"NULL\"")


"""
converts any string into a string surrounded by double quotes and closes any open double quotes within 
the string being converted
"""
def sqlString(input):
    if input == None:
        return '"NULL"'
    output = input.replace('"', '""')
    output = '"' + output + '"'
    return output


"""
Loops through each json file provided on the command line and passes each file
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
            sys.stdout = sys.__stdout__ #redirects output stream to terminal after writing to file
            print("Success parsing " + f)

if __name__ == '__main__':
    main(sys.argv)
