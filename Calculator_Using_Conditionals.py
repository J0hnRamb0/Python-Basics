import time
question = input("What operation do you want to use \n1. Addition + \n2. Subtraction - \n3. Multiplication x \n4. Division / \n5. Quotient // \n6. Remainder \n Choose any : ")
print(question, type(question))

time.sleep(2)

num1 = int(input("enter first Number : " ))
num2 = int(input("enter second Number : "))

if question == "1":
    total = num1 + num2
    print("The sum of {} and {} is {}".format(num1, num2, total))

elif question == "2":
    difference = num1 - num2
    print("The difference of {} and {} is {}".format(num1, num2, difference))

elif question == "3":
    product = num1 * num2 
    print("The product of {} and {} is {} ".format(num1,num2, product))
    
elif question == "4":
    division = num1 / num2
    print("The division of {} and {} is {} ".format(num1,num2 , division))

elif question == "5":
    quotient = num1 // num2 
    print("The quotient of {} and {} is {}".format(num1, num2, quotient))   

elif question == "6":
    remainder = num1 % num2
    print("The remainder of {} and {} is {}".format(num1, num2, remainder))


else:
    print("Invalid input")






