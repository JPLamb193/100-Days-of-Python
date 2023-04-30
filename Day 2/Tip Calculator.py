#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("How much is the bill? $"))
people = int(input("How many ways will it be split? "))
tip = int(input("How much will be tipped? (ex. 12, 10, 5) "))

tip = tip/100
bill = (bill * tip) + bill
perPerson = bill / people
perPerson = round(perPerson, 2)

print(f"Each person should pay: {perPerson:.2f}")

