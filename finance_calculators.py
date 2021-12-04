#Date: 15 July 2021

#Author: Njabulo Nxumalo

#Purpose: Create simple and compound interest calculator.

#Formulae variables: amount = amount including applied interest,
#deposit = principle amount, rate = yearly interest rate, term = time of
#investment(years) or bond(months).

#Compound interest: amount = deposit*(1 + rate)**term.
#Simple interest: amount = deposit*(1 + rate*term).
#Bond repayment: amount = (rate*deposit)/(1 - (1+rate)**(-term)).

import math

print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment     - to calculate the amount of interest you'll earn on interest")
print("bond           - to calculate the amount you'll have to pay on a home loan")
invest_bond = input().lower()

#Investment block.
#Calculates the amount user gets in return given the investment variables.
#User can choose compound or simple interest.
if invest_bond == "investment":
    deposit = float(input("Enter principle amount: "))
    rate = float(input("Enter the interest rate: "))/100
    term = int(input("Enter the number years of investment: "))
    simp_comp = input("Enter 'simple' or 'compound': ").lower()
    
    if simp_comp == "simple":
        amount = deposit*(1 + rate*term)
        print("Amount accumulated ", round(amount,2))
        
    elif simp_comp == "compound":
        amount = deposit*math.pow(1 + rate,term)
        print("Amount accumulated ",round(amount,2))

    else:
        print("Error: Please enter 'simple' or 'compound'.")
        
#Bond repayment block.
#Calculates amount user will pay each month from given input.      
elif invest_bond == "bond":
    deposit = float(input("Enter the value of the house: "))
    rate = float(input("Enter the interest rate: "))/100/12
    term = int(input("Enter the number months to repay: "))
    
    amount = (rate*deposit)/(1 - math.pow(1 + rate, -term))
    
    print("Amount that needs to be repaid each month ", round(amount,2))
    
else:
    print("Error: Please enter 'investment' or 'bond'.")




    
