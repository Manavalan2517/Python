
# Problem_4 :-
# Counting occurrences

num = int(input("Enter a number: "))
cnum = int(input("Which number do you want to count: "))

rem = 0
count = 0

while num > 0:
    rem = int(num) % 10
    if cnum == rem:
        count = count + 1
    num = num / 10
print(count)