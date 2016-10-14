# High scores with nested tables

scores = [("Moe", 1000), ("Larry", 1500), ("Curly", 3000)]
print scores[0]
print scores[1]
print scores[2]

print scores[2][0]

print "Add your name and score to the list!"
name, score = raw_input("Name: "), raw_input("Score: ")
print name
new_value = name, score
scores.append(new_value)
print scores