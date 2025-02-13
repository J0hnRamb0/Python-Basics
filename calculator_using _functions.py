def addition (x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

def quotient(x,y):
    return x//y

def remainder(x,y):
    return x%y

question = input("Welcome to the Calculator program : \nWhat operation do you want to use \n1. Addition + \n2. Subtraction - \n3. Multiplication x \n4. Division / \n5. Quotient // \n6. Remainder \n Choose any : ")



while True:

    question = input("Welcome to the Calculator program : \nWhat operation do you want to use \n1. Addition + \n2. Subtraction - \n3. Multiplication x \n4. Division / \n5. Quotient // \n6. Remainder \n Choose any : ")

    num1 = int(input("enter first number : "))
    num2 = int(input("enter second number : "))
    if question == "1":
        #total = num1 + num2
        print("The sum of {} and {} is {}".format(num1, num2, addition(num1, num2)))

    elif question == "2":
        #difference = num1 - num2
        print("The difference of {} and {} is {}".format(num1, num2, subtraction(num1, num2)))

    elif question == "3":
        #product = num1 * num2 
        print("The product of {} and {} is {} ".format(num1,num2, multiplication(num1, num2)))
    
    elif question == "4":
        #division = num1 / num2
        print("The division of {} and {} is {} ".format(num1,num2 , division(num1, num2)))

    elif question == "5":
        #quotient = num1 // num2 
        print("The quotient of {} and {} is {}".format(num1, num2, quotient(num1, num2)))   

    elif question == "6":
        #remainder = num1 % num2
        print("The remainder of {} and {} is {}".format(num1, num2, remainder(num1, num2)))

    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break

print("\nThanks for Playing!")