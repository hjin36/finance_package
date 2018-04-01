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
	def __repr__(self):
		return "Account: %s have %.2f in %s" % (self.investor.name,self.size,self.issuer.name)
	def deposit(self,amount):
		new_transaction = Transaction(self.issuer,self.investor,amount,"%s deposit %.2f in %s" % (self.investor.name,amount,self))
		self.size += amount
		return new_transaction.note
	def withdrawl(self,amount):
		new_transaction = Transaction(self.investor,self.issuer,amount,"%s withdrawl %.2f in %s" % (self.investor.name,amount,self))
		self.size -= amount
		return new_transaction.note

class Checking_Account(Account):
	def __repr__(self):
		return "[Checking_Account: %s have %.2f in %s]" % (self.investor.name,self.size,self.issuer.name)


