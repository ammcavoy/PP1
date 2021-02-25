SELECT COUNT(*) FROM (
    SELECT DISTINCT Categories.Category
    FROM Categories,Items 
    WHERE Categories.ItemID = Items.ItemID AND
        Items.Currently > 100 AND
        Items.Num_of_Bids > 0
);