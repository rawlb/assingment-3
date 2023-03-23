# this defines the variables
# also it gives a float input
constant = 1 
investment_amount = float(input("Investment Amount: "))
monthly_payment = float(input("Monthly Payment: "))
annual_intrest = float(input("Annual Interest as 0.0: "))
nom_years = float(input("Number of Years: "))

monthly_interest_rate = annual_intrest / 12 / 100
num_months = nom_years * 12

# this print computes the defined variables.
print ("the total amount is", investment_amount * (constant + monthly_interest_rate)**num_months) 