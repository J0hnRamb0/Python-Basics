# Python data have multiple types eg : integer, float, strings, boolean covering the basic part
# We have List, Tuple, Set and Dictionary covering the advanced part

abc1 = 23
print(abc1, type(abc1))

# Type is a predefined function already available in python, which tells us what kind of data we are interacting with.

# Floats are numbers with decimal point in them, they are generally lying between the lower and upper limit of two consecutive numbers

abc2 = 21.12
print(abc2, type(abc2))

abc3 = 21.9876423
print(abc3, type(abc3))

# Strings are alphanumeric and they are always written within inverted quotes.
# Strings can contain alphabets, numbers and characters. They are always enclosed within quotation marks

abc4 = "Jonathon"
print(abc4, type(abc4))

abc5 = "123698714"
abc6 = "103.214"
# abc7 = 213. 33 # we should never have space in between the numbers as it changes its face value and space is a character, so we have to make it a string
print(type(abc5), type(abc6), type(abc6))

# Rules for naming a variable:
# 1. Variable names should always start with a character. 
# 2. Variable names would be unacceptable if start with anumber 
# 3. No special charcter should be used for naming a variable, only underscore is allowed as an exception. 
# 4. Variable names should not contain any keywords like if else, while for etc. as they already have predefined meaning in python

x123 = 48
# x 23 = 10.12
# 1_x23 = "test" 
_123 = "value"
print(_123)

for1 = 23
print(for1)

print("Hello Jonathon! Hope you are doing well. How's things ?")
print('Hello Jonathon!')

#print('Hello Jonathon! Hope you are doing well. How's things ?')
# For cases like above apostrophe can cause concern as it is exactly similar to quotation marks, hence the error in output

print("Hello Jonathon! Hope you are doing well. How's things ?") # way 1

print('Hello Jonathon! Hope you are doing well. How\'s things ?')# Way 2

print('Hello Jonathon! \t\t\tHope you are doing well. How\'s things ?') # \t introduces gap between words

print('Hello Jonathon! \nHope you are doing well. How\'s things ?') # Creates a new line