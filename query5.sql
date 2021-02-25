SELECT COUNT(*) FROM(
    SELECT DISTINCT users.UserID
    FROM users,items
    WHERE 
    users.UserID = items.SellerID
    AND
    users.Rating > 1000
); 