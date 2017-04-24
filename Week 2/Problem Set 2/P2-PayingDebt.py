balance = 3926
annualInterestRate  = 0.2
monthlyInterestRate = annualInterestRate/12.0
minPayment = 10

payOffBalance = False
monthlyPayment = minPayment
while (not payOffBalance):
    debt = balance

    for month in range(1,13):    
        UnpaidBalance = debt - monthlyPayment
        debt = (UnpaidBalance * monthlyInterestRate) + UnpaidBalance
    
    if (debt <= 0):
        payOffBalance = True
    else:
        monthlyPayment += minPayment
    
print('Lowest Payment: ' + str(monthlyPayment))