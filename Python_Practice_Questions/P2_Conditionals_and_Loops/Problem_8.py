
# Problem_8 :-
# To find out whether the given String is Palindrome or not.

string = input("Enter any word: ")
if string[::-1] == string:
    print("Entered string is a Palindrome")
else:
    print("Entered string is not a Palindrome")

#----------------or-------------------------

stringLength = len(string)
count = 0
i = 0
for i in range (stringLength):
    stringLength -= 1
    if string[i] == string[stringLength]:
        count += 1
    
if count == len(string):
    print("Entered string is a Palindrome")
else:
    print("Entered string is not a Palindrome")