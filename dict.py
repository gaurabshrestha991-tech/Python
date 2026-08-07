myDict = {
    "name" : "Gaurab",
    "surname" : "Shrestha",
    "age" : 19,
    "height" : 5.9,
    "course" : "BIT",
    "College" : "Amrit Science Campus",
    "university" : "Tribhuvan University",
}
myDict.update({"city":"Kathmandu"})
myDict.update({"name" : "Geeta"})

new_dict = {"city" : "Pokhara", "age" : "18"}
myDict.update(new_dict)
print(new_dict)

for el in myDict:
     print(el, ":", myDict[el])

print(myDict.get("name"))

print(myDict.values())

