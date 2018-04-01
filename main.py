#! /usr/bin/env python3

from financial_institute import *

wells_fargo = Retail_Bank("wells fargo")
tom = Person("Tom",10000)
wells_fargo.interests["Checking_Interest"] = 0.00
wells_fargo.setAccount(tom,size=5000)
tom.asset[0].deposit(2000)
print(tom.asset[0].withdrawl(1000))
print(tom.asset[0])
