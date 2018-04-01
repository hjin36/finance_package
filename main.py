#! /usr/bin/env python3

from financial_institute import *

wells_fargo = Retail_Bank("wells fargo")
tom = Person("Tom",10000)
wells_fargo.setAccount(tom,size=5000)
wells_fargo.setAccount(tom,size=2000,account_type="Saving_Account")
tom.asset[0].deposit(2000)
print(tom.asset[0].withdrawl(1000),end="\n")
print(tom.asset[0])
tom.asset[0].transfer(500,tom.asset[1])
print(tom.capital)
print(tom.asset)
