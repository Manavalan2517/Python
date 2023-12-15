
#  Problem_4 :-
#  Program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.



p = int(input("Enter the principal amount: "))
r = int(input("Enter the interest rate (in percentage): "))
t = int(input("Enter the time duration (in years): "))

prt = ((p*r*t)/100)
print("Total Interest = ", prt)
print("End Balance = ", (prt + p))