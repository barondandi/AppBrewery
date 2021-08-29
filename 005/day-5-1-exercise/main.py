# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Calculate number of students
# number_of_students = len(student_heights)
number_of_students = 0
for index in student_heights:
  number_of_students += 1
# print(number_of_students)

# Calculate sum of heights
# sum_of_heights = sum(student_heights)
sum_of_heights = 0
for height in student_heights:
  sum_of_heights += height
# print(sum_of_heights)

average_height = sum_of_heights / number_of_students
print(round(average_height))

''' SOLUTION
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
average_height = round(total_height / number_of_students)
print(average_height)
'''