# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# BMI = mass / height^2

#   Example Input
#       weight = 80
#       height = 1.75
#   Example Output
#       80 ÷ (1.75 x 1.75) = 26.122448979591837
#       26

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int( float(weight) / (float(height)**2) )
print(bmi)
