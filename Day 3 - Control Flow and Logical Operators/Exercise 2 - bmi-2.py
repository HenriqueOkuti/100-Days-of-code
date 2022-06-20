# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round((weight)/(height**2))

if (bmi >= 18 and bmi < 22):
  print("Your BMI is {}, you are underweight.".format(bmi))
elif (bmi >= 22 and bmi < 28):
  print("Your BMI is {}, you have a normal weight.".format(bmi))
elif (bmi >= 28 and bmi < 33):
  print("Your BMI is {}, you are slightly overweight".format(bmi))
elif (bmi >= 33 and bmi < 40):
  print("Your BMI is {}, you are obese.".format(bmi))  
elif (bmi >= 40):
  print("Your BMI is {}, you are clinically obese.".format(bmi))
  


