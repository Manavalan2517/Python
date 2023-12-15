

# Problem_10 :-
# Subtract the Product and Sum of Digits of an Integer


num = input("Enter a number: ")
lst = []

for i in num:
    lst.append(int(i))

product = 1
for j in lst:
    product *= int(j)

sum = sum(lst)

print("Product of digits = ", product)
print("Sum of digits = ", sum)
print("Result = ", (product - sum))