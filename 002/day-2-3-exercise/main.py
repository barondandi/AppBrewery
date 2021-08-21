# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# HINT: There are 365 days in a year, 52 weeks in a year and 12 months in a year.
days_per_year = 365
weeks_per_year = 52
months_per_year = 12

# EXAMPLE OUTPUT: "You have 12410 days, 1768 weeks, and 408 months left."
estimated_lifespan = 90
years_left = estimated_lifespan - int(age)
months_left = years_left * months_per_year
weeks_left = years_left * weeks_per_year
days_left = years_left * days_per_year

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

''' SOLUTION
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
'''