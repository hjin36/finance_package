#! /usr/bin/env python3

from fundamental_classes import *

default = {
	 "Checking_Interest" : 0.00,
	 "Saving_Interest" : 0.02,
	 "Transfer_fee" : 0
	 "Simple_Loan" : 0.05
	}

class Bank(Institute):
	pass

class Retail_Bank(Bank):
	def __init__(self,name,capital=0,company_id=0,note="",accounts=[]):
		global reset
		Institute.__init__(self,name,capital,company_id,note)
		self.accounts = accounts
		self.interests = default
	def setAccount(self,investor,account_type="Checking_Account",product_id=0,size=0,note=""):
		if account_type=="Checking_Account":
			new_account = Checking_Account(self.name,self,investor,product_id,size,self.interests["Checking_Interest"],note)
			self.accounts.append(new_account)
		elif account_type=="Saving_Account":
			new_account = Saving_Account(self.name,self,investor,product_id,size,self.interests["Saving_Interest"],note)
			self.accounts.append(new_account)
	def giveLoan(self,investor,loan_type="Simple_Loan",product_id=0,size=0,maturity_days = 365,note=""):
		if loan_type == "Simple_Loan":
			new_loan = Loan(self.name,investor,issuer,product_id,size,maturity_days,self.interests["Simple_Loan"],note)
			

class Account(Product):
	def __init__(self,name,issuer,investor,product_id=0,size=0,interest=0.00,note=""):
		Product.__init__(self,name,issuer,investor,product_id,size,note)
		self.interest = interest
	def __repr__(self):
		return "Account: %s have %.2f in %s" % (self.investor.name,self.size,self.issuer.name)
	def deposit(self,amount):
		new_transaction = Transaction(self.issuer,self.investor,amount,"%s deposit %.2f in %s" % (self.investor.name,amount,self))
		self.size += amount
		return new_transaction.note  #may be changed in the future
	def withdrawl(self,amount):
		new_transaction = Transaction(self.investor,self.issuer,amount,"%s withdrawl %.2f in %s" % (self.investor.name,amount,self))
		self.size -= amount
		return new_transaction.note  #may be changed in the future
	def transfer(self,amount,other):
		new_transaction = Transaction(other.issuer,self.issuer,amount*(1-self.issuer.interests["Transfer_fee"]),note="")
		self.size -= amount*(1-self.issuer.interests["Transfer_fee"])
		other.size += amount*(1-self.issuer.interests["Transfer_fee"])
		self.issuer.capital += amount * self.issuer.interests["Transfer_fee"]

class Checking_Account(Account):
	def __repr__(self):
		return "[Checking_Account: %s have %.2f in %s]" % (self.investor.name,self.size,self.issuer.name)

class Saving_Account(Account):
	def __repr__(self):
		return "[Saving_Account: %s have %.2f in %s, interest = %.2f]" % (self.investor.name,self.size,self.issuer.name,self.interest)
	def payinterest(self):
		new_transaction = Transaction(self.issuer,self.investor,self.interest*self.size,"interest added: %.2f" % (self.interest * self.size))
		self.size += amount
		return new_transaction.note  #may be changed in the future

class Loan(Debt):
	def __init__(self,name,issuer,investor,product_id=0,size=0,maturity_days=1,interest=0.00,note=""):
		Debt.__init__(name,issuer,investor,product_id,size,maturity_days,interest,note)
