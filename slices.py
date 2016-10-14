class Employees:
	def __init__(self, wage, name):
		self.wage = wage
		self.name = name
		print(self.name)
		print(self.wage)
		self.hugh()
		
	def test(self):
		print(self.name)
		
	def hugh(self):
		print("Hugh")
		
	
		
		
emp1 = Employees(1000, "Hugh")
emp2 = Employees(2000, "Jeremy")