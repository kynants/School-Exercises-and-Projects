points = [0, 5, 15, 30, 60]
books = int(input("How many books have you purchased this month? "))

if books == 0:
    print("Number of points earned: ", points[0])
elif books == 1:
    print("Number of points earned: ", points[1])
elif books == 2:
    print("Number of points earned: ", points[2])
elif books == 3:
    print("Number of points earned: ", points[3])
elif books == 4:
    print("Number of points earned: ", points[4])
else:
    print("Ask the front-desk.")