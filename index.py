# Indexer
import random 

word = raw_input("Please enter a word: ") 
print "The word you have chosen is: %s" % word 

high = len(word)
low = -len(word) 

for i in range(1, 10):
	position = random.randrange(low, high) 
	print "word [", position,"]" "\t", word[position]