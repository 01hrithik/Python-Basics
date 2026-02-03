# Subtraction Operator in Python
# Subtraction Symbol : -

# when u want to cut something we used subtraction
# example : you want to buy two things and each thing price is 40 
# you tell your mom to give me money for two ice-cream cones
# so she will give you 40 + 40 = 80
# you are greedy u want one ice-cream cone & one dark chocolate
# so you buy one ice-cream cone for 40 & two 5 star dark chocolate each price 5
# so total price for dark chocolate is 5 + 5 = 10
# now you have given 80 to shopkeeper   
# shopkeeper will give you back the remaining money after your purchase
# so remaining money is 80 - (40 + 10) = 30
# now you enjoy your ice-cream & dark chocolate

# code representation of above example
ice_cream_cone_price = 40
five_star_dark_chocolate_price = 5

total_money_from_mom = ice_cream_cone_price + ice_cream_cone_price
total_purchase_price = ice_cream_cone_price + (five_star_dark_chocolate_price + five_star_dark_chocolate_price)

invoice = total_purchase_price
print("invoice for ice-cream cone & two 5 star dark chocolate is :", invoice)

remaining_money = total_money_from_mom - total_purchase_price
print("remaining money after purchase is :", remaining_money)
# output will be : remaining money after purchase is : 30    

