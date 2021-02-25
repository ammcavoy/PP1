drop table if exists Items;
drop table if exists Sellers;
drop table if exists Bidders;
drop table if exists Bids;
drop table if exists Users;
drop table if exists Categories;


CREATE table Items(
    ItemID STRING PRIMARY KEY,
    SellerID STRING,
    Country STRING,
    Location STRING,
    Name STRING,
    Buy_Price FLOAT,
    First_Bid FLOAT,
    Currently FLOAT,
    Num_of_Bids FLOAT,
    Description STRING,
    Started DATE,
    End DATE,
    FOREIGN KEY (SellerID) REFERENCES Users(UserID));

CREATE table Users(
    UserID STRING PRIMARY KEY,
    Rating INT,
    Country STRING,
    Location STRING);

CREATE table Bids(
    BidderID STRING,
    ItemID STRING,
    Amount FLOAT,
    Time DATE,
    PRIMARY KEY (BidderID, Time),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID));

CREATE table Categories(
    ItemID STRING,
    Category STRING,
    PRIMARY KEY(ItemID, Category)
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID));

.separator |
.import items.dat Items
UPDATE Items SET Buy_Price = NULL WHERE Buy_Price = "NULL";
UPDATE Items SET Description = NULL WHERE Description = "NULL";
.import bids.dat Bids
.import categories.dat Categories
.import users.dat Users
UPDATE Users SET Location = NULL WHERE Location = "NULL";
UPDATE Users SET Country = NULL WHERE Country = "NULL";