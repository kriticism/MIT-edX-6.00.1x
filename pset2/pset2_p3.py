# Author: Kriti Singh | kriti96.singh@gmail.com | ks2259
# Date: June 22, 2017

"""
balance = 320000
annualInterestRate = 0.2
"""
################################

origBalance = balance
monthlyInterestRate = annualInterestRate/12
lowerBound = origBalance/12
upperBound = (origBalance * (1 + monthlyInterestRate)**12)/12.0
_incr = 0.03

while abs(balance) > _incr:
    monthlyFixedPayment = (upperBound + lowerBound)/2
    balance = origBalance
    for i in range(12):
        balance = balance - monthlyFixedPayment + ((balance - monthlyFixedPayment) * monthlyInterestRate)
    if balance > _incr:
        lowerBound = monthlyFixedPayment
    elif balance < -(_incr):
        upperBound = monthlyFixedPayment
    else:
        break
print('Lowest Payment:', round(monthlyFixedPayment, 2))
