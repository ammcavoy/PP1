python3 your_new_favorite_parser.py ebay_data/items-*.json
sort users.dat -o sortedusers.dat
uniq sortedusers.dat users.dat
rm sortedusers.dat
sort categories.dat -o sortedcategories.dat
uniq sortedcategories.dat categories.dat
rm sortedcategories.dat