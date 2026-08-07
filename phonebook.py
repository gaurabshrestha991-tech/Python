phonebook = {
    "Ram" : 98234124,
    "Shyam" : 984941,
    "Hari" :  564941,
    "Gita" : 6498461,
    "Sita" : 165456,
    "Rita" : 561986
}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Show All Contacts")
    print("4. Exit")

    print(" ")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print(" ")
        name = input("Enter name: ")
        number = int(input("Enter number: "))
        phonebook[name] = number
        print("Number saved successfully")

    elif choice == 2:
        print(" ")
        name = input("Enter name: ")

        if name in phonebook:
            print("Phone Number:", phonebook[name])
        else:
            print("Contact not found")
        
    elif choice == 3:
        print(" ")
        for name, number in phonebook.items():
            print(name, ":", number)

    elif choice == 4:
        print(" ")
        print("Exiting....")
        break

    else:
        print("Invalid Choice")