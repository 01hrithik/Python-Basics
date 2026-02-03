# Multiplication operator implementation

# Multiplication symbol : *

# wehen you have to quantities to calculate that time used multiplication

# example : in day-trading you purchase nifty 50 one quintiy 65 units comes
# u think now market will go down so u choose put option of nifty 50
# put option price is 150 rs per unit
# so total price for 65 units will be 65 * 150 = 9750 rs
# now u give 9750 rs to broker & he will purchase put option for u
# now market goes down & u sell ur put option at 200 rs per unit
# hence u made 50 rs profit per unit
# so total profit for 65 units will be 65 * 50 = 3250 rs
# now ur porfolio  value is increased by 3250 rs
# now u r happy with ur profit & u decided to book ur profit

balance = 100000
stock_quantity = 65
put_option_price_per_unit = 150
total_put_option_price = stock_quantity * put_option_price_per_unit
booked_profit_ammount = stock_quantity * 50
porofolio = balance + booked_profit_ammount
print("total put option price for 65 units is :", total_put_option_price)
print("total booked profit after selling put option is :", booked_profit_ammount)
print("total porfolio value after booking profit is :", porofolio)





