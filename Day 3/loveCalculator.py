# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
score1 = 0
score2 = 0
love = ("L", "l", "O", "o", "V", "v", "E", "e")
true = ("T", "t", "R", "r", "U", "u", "E", "e")
for x in name1:
    if x in true:
        score1 += 1
    if x in love:
       score2 += 1
for x in name2:
    if x in true:
       score1 += 1
    if x in love:
       score2 += 1
scoreTotal = int(str(score1) + str(score2))
if (scoreTotal < 10) or (scoreTotal >  90):
       print(f"Your score is {scoreTotal}, you go together like coke and mentos.")
elif (scoreTotal > 40) and (scoreTotal < 50):
       print(f"Your score is {scoreTotal}, you are alright together.")
else:
       print(f"Your score is {scoreTotal}.")
