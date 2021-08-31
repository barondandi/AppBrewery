#For Loop with Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)

# For loop with range
# The last number is NOT included
for number in range(1, 5):
  print(number)

for number in range(1, 11, 3):
  print(number)


# Gauss way of adding 1-100
total = 0
for number in range(1, 101):
  total += number
print(total)