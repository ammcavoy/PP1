/*
Find the number of auctions belonging to exactly four categories
*/
SELECT COUNT(*)
FROM (
    SELECT COUNT(Category) as 'c'
    FROM Categories
    GROUP BY ItemID
) as 'numCats'
WHERE numCats.c = 4;