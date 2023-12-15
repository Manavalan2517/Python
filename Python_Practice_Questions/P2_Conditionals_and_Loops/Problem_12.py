
# Problem_12 :-
# Take integer inputs till the user enters 0 and print the sum of all numbers (HINT: while loop)

print("Press 0 to stop the loop")
lst = []

while True:
    num = int(input("Enter a number: "))
    lst.append(num)
    if num == 0:
        break

print("Sum of all number = ",sum(lst))