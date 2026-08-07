tuple = (1,2,3,4,5,6,7)
print(tuple[6])

#tuple[6] = 7      #Not allowed in tuple

#SLICING 
print(tuple[1:4])
print(tuple[:])
print(tuple[1:])
print(tuple[:6])

#Negative slicing
print(tuple[-5:-2])
print(tuple[:-1])
print(tuple[-1:])


#Tuple Methods

print(tuple.index(7)) # Returns the index of first occurance 

marks = (90,60,80,50,60) 
print(marks.count(60))      # Counts the total occurance of the element


