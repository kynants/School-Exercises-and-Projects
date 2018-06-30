print("Enter the monthly cost for the following:")

loanPayment = int(input("Loan Payment: "))
insurance = int(input("Insurance: "))
gas = int(input("Gas: "))
oil = int(input("Oil: "))
tires = int(input("Tires: "))
maintenance = int(input("Maintenance: "))

print("Your annual cost for everything is $", (loanPayment + insurance + gas + oil + tires + maintenance) * 12)