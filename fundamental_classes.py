#! /usr/bin/env python3

#developer : line 73 last time
class Entity:
	def __init__(self,name,capital=0,note=""):
		self.name = name
		self.capital = capital  #capital is exactly cash account for any entity;
		self.asset=[]
		self.liability=[]
		self.note = note
	def liquidity(self):
		liquiditysum = self.capital
		for i in self.asset:
			liquiditysum += i.size
		for i in self.liability:
			liquiditysum -= i.size
		return liquiditysum
	def raiseDebt(self,debtname,investor,product_id=0,size=0,maturity_days=1,interest=0.00):
		new_debt = Debt(debtname,self,investor,product_id,size,maturity_days,interest)
		self.liability.append(new_debt)
		investor.asset.append(new_debt)
		self.capital += size

class Person(Entity):
	def __init__(self,name,capital=0,person_id=0,note=""):
		Entity.__init__(self,name,capital,note)
		self.id = person_id
	def __str__(self):
		return "Person: %s, Capital: %.2f" % (self.name, self.capital)

class Institute(Entity):
	def __init__(self,name,capital=0,company_id=0,note=""):
		Entity.__init__(self,name,capital,note)
		self.id = company_id
	def __str__(self):
		return "Institute: %s, Capital: %.2f" % (self.name, self.capital)

class Non_Financial(Institute):
	pass


class Product:
	def __init__(self,name,issuer,investor,product_id=0,size=0,note=""):
		self.name = name
		self.issuer = issuer
		self.investor = investor
		self.id = product_id
		self.size = size
		self.note = note
	def __str__(self):
		return "Product: %s, %s get %.2f from %s" % (self.name, self.issuer.name, self.size, self.investor.name)

class Debt(Product):
	def __init__(self,name,issuer,investor,product_id=0,size=0,maturity_days=1,interest=0.00,note=""):
		Product.__init__(self,name,issuer,investor,product_id,size,note="")
		self.maturity_days = maturity_days
		self.interest = interest
	def __str__(self):
		return "Debt: %s, %s raised %.2f from %s, maturity %d days, interest: %.5f" % (self.name,self.issuer.name,self.size,self.investor.name,self.maturity_days, self.interest)
	def __repr__(self):
		return "%s: %s" % (self.name,self.investor)
	def repay(self,size):
		self.size -= size
		self.issuer.capital -= size
		self.investor.capital += size
		if self.size == 0:
			self.issuer.liability.remove(self)
			self.investor.asset.remove(self)
	def payinterest(self):
		self.issuer.capital -= self.size * self.interest
		self.investor.capital += self.size * self.interest

class Industry():
	def __init__(self,name,*args):
		self.name = name
		self.company_list = list(args)
	def addcompany(self,company):
		if company in self.company_list:
			raise ValueError("already have the same company")
		else:
			self.company_list.append(company)

if __name__ == "__main__":
	tom = Person("Tom",10000)
	goldman = Institute("Goldman Sachs",100000)
	jpmorgan = Institute("J.P. Morgan",50000)
	goldman.raiseDebt("IOU",tom,0,10000,60,0.1)
	Financial_service = Industry("Financial_service",goldman)
	Financial_service.addcompany(jpmorgan)
	print([self.name for self in Financial_service.company_list])
