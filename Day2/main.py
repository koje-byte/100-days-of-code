bill=float(input("Welcome to the tip calculator!\nWhat is the total bill amount?\n$:"))
Tip=int(input("How much would you like to tip?\nPercent:"))
Tip=Tip/100
num_of_poeple=int(input("How many people to split the bill ?\nPeople:"))
price_per_person=(bill+(bill*Tip))/num_of_poeple
print("Each person should pay:",f"{price_per_person:.2f}")
