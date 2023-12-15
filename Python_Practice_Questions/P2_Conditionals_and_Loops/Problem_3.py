
# Problem_3 :-
# Fibonacci Series


num = int(input("Enter a number: "))

prev1 = 0
prev2 = 1


for i in range(2, num):
    result = prev1 + prev2
    prev1 = prev2
    prev2 = result

print(result)