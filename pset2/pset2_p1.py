# Author: Kriti Singh | kriti96.singh@gmail.com | ks2259
# Date: June 22, 2017

balance = 484
monthlyPaymentRate = 0.04
annualInterestRate = 0.2

for i in range(12):
    balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12.0))
print "Remaining balance:",  round(balance, 2)
