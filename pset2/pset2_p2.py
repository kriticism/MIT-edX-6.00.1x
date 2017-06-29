# Author: Kriti Singh | kriti96.singh@gmail.com | ks2259
# Date: June 22, 2017

"""
balance = 3329
annualInterestRate = 0.2
"""
################################

origBalance = balance
monthlyFixedPayment = 0
monthlyInterestRate = annualInterestRate/12               # interest is compounded monthly

while balance > 0:
    for i in range(12):
        balance = balance - monthlyFixedPayment + ((balance - monthlyFixedPayment) * monthlyInterestRate)
    if balance > 0:                                       # monthly payment not enought for 1 year
	monthlyFixedPayment += 10
        balance = origBalance
    elif balance <= 0:
        break

print('Lowest Payment:', monthlyFixedPayment)
