
print("_________________________________________")
print("|     Welcome to the tip calculator!    |")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

total = float(input("What was the total bill amount ? : $"))
tip = int(input("What would you like to tip the waiter ? : "))

if tip < 10:
    print("Tip must be atleast 10%!")
else:
    pep = int(input("Enter the number of people, who are paying the bill ? : "))
    tobil = total * ((100 + tip) / 100) / pep
    tobil = round(tobil, 3)
    print(f"Each person should pay ${tobil}!")

