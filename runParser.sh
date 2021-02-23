python skeleton_parser2.py ebay_data/items-*.json
sort bidders.dat -o sortedbidders.dat
uniq sortedbidders.dat bidders.dat
rm sortedbidders.dat
sort sellers.dat -o sortedsellers.dat
uniq sortedsellers.dat sellers.dat
rm sortedsellers.dat