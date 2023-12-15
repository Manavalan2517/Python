
# Problem_5 :-
# Reverse

num = int(input("Enter a number: "))
print(str(num)[::-1])

# ------------or-----------------
while int(num) > 0:
    rem = int(num) % 10
    print(rem,end="")
    num /= 10