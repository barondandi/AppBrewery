#Data Types

#String
"Hello"
# Subscript: method to pull a character out of a string (we start counting at 0):
print("Hello"[0])
print("Hello"[4])
print("Hello"[len("Hello") - 1])
print("123" + "456")

#Integer
123
print(123 + 456)
# We can divide long numbers with underscores to make it easier for us to read
print(123_456)

#Float
3.14159

#Boolean (start with capital letter and no quotation marks)
True
False

#Type Errors
num_char = len(input("What is your name?\n"))
# print("Your name has " + num_char + " characters.")
# This gives me this error: TypeError: can only concatenate str (not "int") to str
print("num_char type is:")
print(type(num_char))
new_num_char = str(num_char)
print("new_num_char type is:")
print(type(new_num_char))
print("Your name has " + new_num_char + " characters.")

#Type Checking
# type()

#Type Conversion (TYPECASTING)
# str()
# int()
# float()
# bool()

print(70 + float("70.15"))
print(str(123) + str(456))