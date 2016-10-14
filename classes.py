# Revision on classes
class Employees:
	emmCount = 0
	
	def __init__(self, name, age):
		self.name = name 
		self.age = age
		Employees.emmCount += 1
		print(name)
		print(age)
		self.displayCount()
		
	def displayCount(self):
		print("The total number of employees is ", + int(Employees.emmCount))
		weight = 2
		build = "slight"
		
	def what(self, weight, build):
		self.weight * 2 
		print(self.weight)
		print("Should return 4")

Employees("Hugh", "25")
Employees("Jeremy", "25")
Employees("Louise", "26")
		
	