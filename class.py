
class Employee:
	def __init__(self, name, salary, rank):
		self.name = name 
		self.salary = salary
		self.rank = rank
		print name, salary, rank 
	
emp1 = Employee("Hugh", 35000, "PC")
emp2 = Employee("Jeremy", 60000, "Cyber security consultant")