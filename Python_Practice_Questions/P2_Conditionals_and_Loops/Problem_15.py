# Problem_15 :- 
# Calculate Discount Of Product

i = 0
lst = []
while True:
    i = i+1
    num = int(input("Enter number "+ str(i) +": "))
    lst.append(num)
    brk = input("Do you want add another number (y/n): ").lower()
    while brk not in ['y','n']:
        brk = input("Do you want add another number (y/n): ").lower()
    if brk == 'n':
        break
numerator = sum(lst)
denominator = len(lst)
print(numerator/denominator)