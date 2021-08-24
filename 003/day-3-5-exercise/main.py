# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Change the names to lowecase
lc_name1 = name1.lower()
lc_name2 = name2.lower()

# Join the two names to make counting easier
name12 = lc_name1 + lc_name2

# Counter 1: TRUE
count1 = 0
count1 += name12.count("t")
count1 += name12.count("r")
count1 += name12.count("u")
count1 += name12.count("e")

# Counter 2: LOVE
count2 = 0
count2 += name12.count("l")
count2 += name12.count("o")
count2 += name12.count("v")
count2 += name12.count("e")

# Score
score = int(str(count1) + str(count2))

# Score interpretation
if score <= 10 or score >=90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

'''SOLUTION
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
'''