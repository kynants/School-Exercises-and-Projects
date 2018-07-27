import time

# Ticket Prices
ticket_a_price = 20
ticket_b_price = 15
ticket_c_price = 10

'''
Amount of Seats
seat_a = 300
seat_b = 500
seat_c = 200
'''

# PROMPTS AND VALIDATIONS
# Prompt A
seat_a = int(input("How many tickets were sold for A seats? "))

# Validation A
while seat_a < 0 or seat_a > 300:
    print("Error: Invalid number of seats.")
    time.sleep(2)
    seat_a = int(input("Please enter a valid number of seats: "))

# Prompt B
seat_b = int(input("How many tickets were sold for B seats? "))

# Validation B
while seat_b < 0 or seat_b > 500:
    print("Error: Invalid number of seats.")
    time.sleep(2)
    seat_b = int(input("Please enter a valid number of seats: "))

# Prompt C
seat_c = int(input("How many tickets were sold for C seats? "))

# Validation C
while seat_c < 0 or seat_c > 200:
    print("Error: Invalid number of seats.")
    time.sleep(2)
    seat_c = int(input("Please enter a valid number of seats: "))

print("The amount of income generated from ticket sales: "
      "${}".format((seat_a * ticket_a_price) + (seat_b * ticket_b_price) +
                  (seat_c * ticket_c_price)))
time.sleep(4)