# Given a list of items, write a script to remove all duplicate elements without using a set.

items = [1,2,3,3,4,4,5,1,7,7,8,9,8,10,6]

unique_items = []

for item in items:
    if item not in unique_items:        #Check whether the current item is NOT already present in the list
        unique_items.append(item)

unique_items.sort() 

print("List without duplicates:",  unique_items) 