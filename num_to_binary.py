# Converting number to binary form

number = int(input("Enter a Number: "))

# converting number to binary 
binary_representation = bin(number)[2: ]

# Display the result
print(f"Binary representation of {number} is: {binary_representation}")


# Generating number from binary digits

Num2 = input("Enter Binary Number: ")

# converting binary to decimal

decimal_number = int(Num2, 2)

print(f"Decimal representation of {Num2} is: {decimal_number}")