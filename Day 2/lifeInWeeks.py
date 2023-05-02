# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ageWorking = int(age)
daysWorking = ageWorking * 365
weeksWorking  = ageWorking * 52
monthsWorking = ageWorking * 12
ageTotal = 90
daysTotal = 365 * ageTotal
weeksTotal = 52 * ageTotal
monthsTotal = 12 * ageTotal
ageRemaining = ageTotal - ageWorking
weeksRemaining = weeksTotal - weeksWorking
daysRemaining = daysTotal - daysWorking
monthsRemaining = monthsTotal - monthsWorking
print(f"You have {daysRemaining} days, {weeksRemaining} weeks, and {monthsRemaining} months left.")
