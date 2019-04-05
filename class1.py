class Calculator:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def add(self):
		print (self.a+self.b)
	def mul(self):
		print (self.a*self.b)
	def sub(self):
		if(self.a>self.b):
			print(self.a-self.b)
		elif(self.b>self.a):
			print(self.b-self.a)
	def div(self):
		if(self.a>self.b):
			print(self.a/self.b)
		elif(self.b>self.a):
			print(self.b/self.a)

a = int(input("a = "))
b = int(input("b = "))
p1 = Calculator(a,b)
p1.add()
p1.sub()
p1.mul()
p1.div()


