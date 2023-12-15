
# Problem_6 :-
# Calculator

while True:
    print("\n\nTo ADD any two numbers press ( + )")
    print("To SUBTRACT any two numbers press ( - )")
    print("To MULTIPLY any two numbers press ( * )")
    print("To DIVIDE any two numbers press ( / )")
    print("To find Reminder of any two numbers press ( % )")
    choose = input('\nChoose any one: ')
    while choose not in ['+', '-', '*', '/', '%']:
        print("INVALID INPUT")
        choose = input("\nChoose any one: ")
    
    num1 = int(input("\nEnter number 1: "))
    num2 = int(input("Enter number 2: "))
    
    if choose == '+':
        print("=============================")
        print("Added value = ",(num1 + num2))
        print("=============================")
    if choose == '-':
        print("=============================")
        print("Subtracted value = ",(num1 - num2))
        print("=============================")
    if choose == '*':
        print("=============================")
        print("Multiplied value = ",(num1 * num2))
        print("=============================")
    if choose == '/':
        print("=============================")
        print("Divided value = ",(num1 / num2))
        print("=============================")
    if choose == '%':
        print("=============================")
        print("Remainder value = ",(num1 % num2))
        print("=============================")
    isbreak = input("Do you want to try again: ").lower()
    while isbreak not in ['y', 'n']:
        isbreak = input("Do you want to try again: ").lower()
    if isbreak == "n":
        break