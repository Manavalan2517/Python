
# Problem_11 :-
# Input a number and print all the factors of that number (use loops).

num = int(input("Enter a number: "))

for i in range (1, num + 1):
    if num % i == 0:
        print(i, end=' ')