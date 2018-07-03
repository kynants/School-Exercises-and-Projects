len1 = int(input("What is the rectangle 1's length? "))
wid1 = int(input("What is the rectangle 1's width? "))
len2 = int(input("What is the rectangle 2's length? "))
wid2 = int(input("What is the rectangle 2's width? "))

rect1 = len1 * wid1
rect2 = len2 * wid2

if rect1 > rect2:
    print("Rectangle 1 is bigger.")
elif rect1 < rect2:
    print("Rectangle 2 is bigger.")
else:
    print("They are the same.")