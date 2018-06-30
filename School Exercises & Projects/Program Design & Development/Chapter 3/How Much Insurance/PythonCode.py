# This program will ask how much your house costs, and recommend you save at least 80% of what it would cost to replace it.

percentage = 0.8

cost = int(input("Enter how much your house is worth: "))
cost *= percentage
print("You should save $", cost, " to replace your house.")