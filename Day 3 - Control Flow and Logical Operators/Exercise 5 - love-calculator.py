# 🚨 Don't change the code below 👇
from xml.etree.ElementTree import tostring


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

count1 = 0
count2 = 0

count1 += name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e')
count2 += name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e')

count1 += name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')
count2 += name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')

count1 = str(count1)
count2 = str(count2)

total = count1 + count2

totalint = int(total)

if (totalint < 10 or totalint > 90):
    print("Your score is {}, you go together like coke and mentos.".format(total))
elif (totalint > 40 and totalint < 50):
    print("Your score is {}, you are alright together.".format(total))
else:
    print("Your score is {}".format(total))
