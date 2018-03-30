#! /usr/bin/env python3

class Entity:
	def __init__(self,name,capital=0):
		self.name = name
		self.capital = capital  #capital is exactly cash account for any entity;
		self.asset=[]
		self.liability=[]
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
	def __init__(self,name,capital=0,person_id=0):
		Entity.__init__(self,name,capital)
		self.id = person_id
	def __str__(self):
		return "Person: %s, Capital: %.2f" % (self.name, self.capital)

class Institute(Entity):
	def __init__(self,name,capital=0,company_id=0):
		Entity.__init__(self,name,capital)
		self.id = company_id
	def __str__(self):
		return "Institute: %s, Capital: %.2f" % (self.name, self.capital)

class Product:
	def __init__(self,name,issuer,investor,product_id=0,size=0):
		self.name = name
		self.issuer = issuer
		self.investor = investor
		self.id = product_id
		self.size = size
	def __str__(self):
		return "Product: %s, %s get %.2f from %s" % (self.name, self.issuer.name, self.size, self.investor.name)

class Debt(Product):
	def __init__(self,name,issuer,investor,product_id=0,size=0,maturity_days=1,interest=0.00):
		Product.__init__(self,name,issuer,investor,product_id,size)
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
		self.issuer.capital -= self.size * interest
		self.investor.capital += self.size * interest



if __name__ == "__main__":
	tom = Person("Tom",10000)
	goldman = Institute("Goldman Sachs",10 ** 10)
	goldman.raiseDebt("IOU",tom,0,10000,60,0.1)
	print(goldman.liquidity())
	print(goldman.capital)
	goldman.liability[0].repay(10000)
	print(goldman.liability)
	print(tom.asset)
