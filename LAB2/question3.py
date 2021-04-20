
#price of a house is $1M.if buyer has good credit,they need too put down 10% otherwise they need to put down 20%.print the down payment
price=100000
good_credit=str(input("enter if you have good credit or not"))
if good_credit=="true":
    down_payment=(10*price)/100
else:
    down_payment=(20*price)/100

print(down_payment)




