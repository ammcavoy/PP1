drop table if exists Items;
drop table if exists Sellers;
drop table if exists Bidders;
drop table if exists Bids;

CREATE table Items(
    ItemID STRING,
    SellerID STRING,
    Country STRING,
    Location STRING,
    Name STRING,
    Buy_Price FLOAT,
    First_Bid FLOAT,
    Currently FLOAT,
    Num_of_Bids FLOAT,   //should this be int?
    Description STRING,
    Started DATE,
    End DATE,
    Categories STRING
    PRIMARY KEY (ItemID),
    FOREIGN KEY (SellerID) REFERENCES Sellers(UserID));

CREATE table Sellers(
    UserID STRING,
    Rating INT,
    Country STRING,
    Location STRING,
    PRIMARY KEY (UserID));

CREATE table Bidders(
    UserID STRING,
    Rating INT,
    Country STRING,
    Location STRING
    PRIMARY KEY (UserID));

CREATE table Bids(
    BidderID STRING,
    ItemID STRING,
    Amount FLOAT,
    Time DATE,
    PRIMARY KEY (BidderID, Time)
    FOREIGN KEY (BidderID) REFERENCES Bidders(UserID)
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID));