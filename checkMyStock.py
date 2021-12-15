from login import login
rs = login()
my_stocks = rs.build_holdings()
print(my_stocks)
