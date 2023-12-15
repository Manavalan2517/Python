

# Problem_13 :-
# Take integer inputs till the user enters 0 and print the largest number from all.

print("Press 0 to stop the loop")
max = 0
while True:
    num = int(input("Enter a number: "))
    if num > max:
        max = num
    if num == 0:
        break
print("Max = ", max)