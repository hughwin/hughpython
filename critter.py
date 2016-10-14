# demonstrates the use of critters 
class Critter(object): 
	""" A virtual pet"""
	def __init__(self, name):
		print ("A new critter has been born!")
		self.name = name
		
	def __str__(self):
		rep = "Critter onject\n"
		rep += "name: " + self.name + "\n" 
		return rep
		
		
	
	
	
	def talk(self):
		print ("Hi, I'm the first instance of class critter")
		
crit1 = Critter("poochie")
crit1.talk()

crit2 = Critter("randolph")
crit2.talk()

print("Prinitng crit1: ") 
print(crit1) 

print("Directly accessing crit1.name: ") 
print(crit1.name)

print("Prinitng crit2: ") 
print(crit2) 

print("Directly accessing crit2.name: ") 
print(crit2.name)

raw_input("Press the enter key to exit")

