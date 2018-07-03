''' Python does not support switch/case statements, and therefore the programmer
must use if-elif-else statements instead. '''

romNum = int(input("Enter a number between 1-10: "))

if romNum == 1:
    print("I")
elif romNum == 2:
    print("II")
elif romNum == 3:
    print("III")
elif romNum == 4:
    print("IV")
elif romNum == 5:
    print("V")
elif romNum == 6:
    print("VI")
elif romNum == 7:
    print("VII")
elif romNum == 8:
    print("VIII")
elif romNum == 9:
    print("IX")
elif romNum == 10:
    print("X")
else:
    print("Error. Invalid Number.")