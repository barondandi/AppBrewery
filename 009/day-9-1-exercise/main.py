student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# 1: Create an empty dictionary called student_grades.
student_grades = {}

# 2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    grade = ""
    if student_scores[key] >= 91:
        grade = "Outstanding"
    elif student_scores[key] >= 81:
        grade = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade

# 🚨 Don't change the code below 👇
print(student_grades)

'''SOLUTION
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to covert scores into grades.👇
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    

#Don't change the code below 👇
print(student_grades)
'''