actual_cost=float(input("please write down the price of the product"))
sales_amount=float(input("please write down the sales amount of the product"))

if(sales_amount>actual_cost):
    amount=sales_amount-actual_cost
    print("total profit = {0}".format(amount))
else:
    print("no profit")