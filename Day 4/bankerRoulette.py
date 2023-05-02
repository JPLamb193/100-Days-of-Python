# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
namesLength = len(names)
randNum = random.randint(0, namesLength)

print(f"{names[randNum]} is going to buy the meal today!")
