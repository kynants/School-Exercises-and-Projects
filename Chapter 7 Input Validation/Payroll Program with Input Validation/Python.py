# IMPORT
# https://docs.python.org/3/library/time.html
import time

# PAY RATE PROMPT
pay_rate = float(input("Enter your hourly pay rate: "))

# PAY RATE VALIDATION
while pay_rate < 7.5 or pay_rate > 18.25:
    pay_rate = float(input("Error. Please enter a valid wage: "))

# HOURS WORKED PROMPT
hrs_worked = int(input("How many hours did you work? "))

# HOURS WORKED VALIDATION
while hrs_worked < 0 or hrs_worked > 40:
    print("Error. Number of hours worked must be from 0 to 40.")
    time.sleep(2)
    hrs_worked = float(input("Please enter a valid number of hours worked: "))

# THE PROGRAM FINALLY DISPLAYS THE DAY'S WAGE
print("Your weekly salary is: ${}".format(pay_rate * hrs_worked))
