#! /usr/bin/env python3

from fundamental_classes import *

class Bank(Institute):
	pass

class Retail_Bank(Institute):
	def __init__(self,name,capital=0,company_id=0,note="",accounts=[]):
		Institute.__init__(self,name,capital,company_id,note)
		self.accounts = accounts
		self.interests = {}
	def setAccount(self,investor,account_type="Checking_Account",product_id=0,size=0,note=""):
		if account_type=="Checking_Account":
			new_account = Checking_Account(self.name,self,investor,product_id,size,self.interests["Checking_Interest"],note)
			self.accounts.append(new_account)

class Account(Product):
	def __init__(self,name,issuer,investor,product_id=0,size=0,interest=0.00,note=""):
		Product.__init__(self,name,issuer,investor,product_id,size,note)
		self.interest = interest
		issuer.capital += size
		investor.capital -= size
		issuer.liability.append(self)
		investor.asset.append(self)
	def __repr__(self):
		return "Account: %s have %.2f in %s" % (self.investor.name,self.size,self.issuer.name)

class Checking_Account(Account):
	def __repr__(self):
		return "Checking_Account: %s have %.2f in %s" % (self.investor.name,self.size,self.issuer.name)


if __name__ == "__main__":
	wells_fargo = Retail_Bank("wells fargo")
	tom = Person("Tom",10000)
	wells_fargo.interests["Checking_Interest"] = 0.00
	wells_fargo.setAccount(tom,size=5000)
	print(tom.capital,tom.asset,wells_fargo.accounts,wells_fargo.liability,wells_fargo.capital)
