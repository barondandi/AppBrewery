# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

two_digit_string = str(two_digit_number)
# previous step is unneeded, as input returns an string. We can verify with the type() function
two_digit_sum = int(two_digit_string[0]) + int(two_digit_string[1])
print(two_digit_sum)

''' SOLUTION
#Check the data type of two_digit_number
print(type(two_digit_number))

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits togeter
two_digit_number = first_digit + second_digit

print(two_digit_number)
'''