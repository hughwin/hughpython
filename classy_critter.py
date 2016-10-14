# Classy Critter
# Demonstrates class attributes and static methods

class Critter(object):
    """A virtual pet"""
    total = 0

    @staticmethod   
    def status():
        print("\nThe total number of critters is", Critter.total)
        
    def __init__(self, name, mood):
        print("A critter has been born!")
        self.name = name
        self.__mood = mood 
        print(mood)
        print(self.__mood)
        Critter.total += 1
    
    def talk(self):
    	print("\n I'm", self.name)
    	print("Right now, I feel", self.__mood, "\n")
    	

#main
Critter("Hugh", "happy")