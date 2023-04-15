import math
import random as rand
Opertations = ["+", "-", "*", "/"]

operator = None
output = None
operator = rand.choice(Opertations)
Streak  = 0

while output is None or output != int(output):
    if operator == "+" or  operator == "-":
        num1 = rand.randint(1,100)
        num2 = rand.randint(1,100)
    elif operator == "*":
        num1 = rand.randint(2,25)
        num2 = rand.randint(2,25)
    elif operator == "/":
        num1 = rand.randint(2, 25)
        num2 = rand.randint(2,25)
    output = eval(str(num1)+operator+str(num2))
print((str(num1)+operator+str(num2)),"=")



while True:
    User_input = input("Enter your answer: ")
    try:
        User_input = int(User_input)
        break
    except ValueError:
        print("That's not a valid number. Please enter a valid number.")

if User_input == output:
    print("Correct")
    Streak += 1
else:
    print("Incorrect")
    print("The correct answer is",output)
    Streak = 0

print("Your streak is",Streak)