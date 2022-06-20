#Instructions
#I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#https://waitbutwhy.com/2014/05/life-weeks.html
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left.
#Where x, y and z are replaced with the actual calculated numbers.

#   Example Input
#       56
#   Example Output
#       You have 12410 days, 1768 weeks, and 408 months left.

#Hint
#There are 365 days in a year, 52 weeks in a year and 12 months in a year.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

remaining_years = 90 - int(age)
x_days = 365 * remaining_years
y_weeks = 52 * remaining_years
z_months = 12 * remaining_years

print(f"You have {x_days} days, {y_weeks} weeks, and {z_months} months left.")