import random

randNum1 = random.uniform(0, 10)
randNum2 = random.uniform(0, 10)

print(randNum1)
print(randNum2)

answer = randNum1 + randNum2
userInput = int(input("Add these two numbers together. "))

while userInput != answer:
    answerAgain = int(input("Wrong answer. Try again. "))

print("Correct answer!")