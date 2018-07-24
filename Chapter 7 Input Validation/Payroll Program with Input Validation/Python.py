# PAY RATE PROMPT
payRate = float(input("Enter your hourly pay rate: "))

# PAY RATE VALIDATION
while payRate < 7.5 and payRate > 18.25:
    payRate = float(print("Error. Please enter a valid wage: "))

# HOURS WORKED PROMPT
hrsWork = int(input("How many hours did you work? "))

# HOURS WORKED VALIDATION
while hrsWork < 0 and hrsWork > 40:
    