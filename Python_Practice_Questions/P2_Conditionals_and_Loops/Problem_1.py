
# Problem_1 :-
# Take 2 numbers as input and print the largest number.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

max = 0

if num1 > num2:
    max = num1
else:
    max = num2

print(max)