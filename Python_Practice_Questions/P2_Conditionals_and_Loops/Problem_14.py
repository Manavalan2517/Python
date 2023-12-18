# Problem :- 14
# Calculate Electricity Bill

unit = int(input("Enter the Total units: "))

if unit <= 100:
    amount = unit * 10
    print("Amount =",amount)

elif unit > 100 and unit <=200:
    amount1 = 100 * 10
    unit -= 100
    amount2 = unit * 15
    print("Amount =",(amount1 + amount2))


elif unit > 200 and unit <= 300:
    amount1 = 100 * 10
    amount2 = 100 * 15
    unit -= 200 
    amount3 = unit * 20
    print("Amount =",(amount1 + amount2 + amount3))

else:
    amount1 = 100 * 10
    amount2 = 100 * 15
    amount3 = 100 * 20
    unit -= 300
    amount4 = unit * 25
    print("Amount =",(amount1 + amount2 + amount3 + amount4))