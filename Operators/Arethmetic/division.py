# Division symbol : /
# when you have to break | spearte  something you used division operator

# example : you take loan from bank for youre trading
# loan ammount is 1 lakh rs
# bank interest rate is 12% per annum
# so after one year u have to pay back to bank 1,12,000 rs
# now u want to pay back to bank in 12 equal monthly installments
# so each month installment will be 1,12,000 / 12 = 9,333.33 rs
# now u pay 9333.33 rs to bank each month for next twelve months       





loan_ammount = 100000
interest_rate = 0.12    
total_payable_ammount = loan_ammount + (loan_ammount * interest_rate)
monthly_installment = total_payable_ammount / 12
print("total payable ammount after one year is :", total_payable_ammount)
print("monthly installment to be paid to bank is :", monthly_installment)
