drop table if exists Item;
drop table if exists Seller;
drop table if exists Bidder;
drop table if exists Bid;

create table Item(
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
    PRIMARY KEY ItemID,
    FOREIGN KEY SellerID REFERENCES Seller);

create table Seller(
    UserID STRING,
    Rating INT,
    Country STRING,
    Location STRING
    PRIMARY KEY UserID);

create table Bidder(
    UserID STRING,
    Rating INT,
    Country STRING,
    Location STRING
    PRIMARY KEY UserID);

create table Bid(
    BidderID STRING,
    ItemID STRING,
    Amount FLOAT,
    Time DATE,
    PRIMARY KEY (BidderID, Time)
    FOREIGN KEY BidderID REFERENCES Bidder
    FOREIGN KEY ItemID REFERENCES Item);