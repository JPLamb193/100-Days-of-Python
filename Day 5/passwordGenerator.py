#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

totalNr = nr_letters + nr_symbols + nr_numbers
password = []
replacedSpots = []
for x in range(0, totalNr):
    currentLetter = letters[random.randint(0, (len(letters)-1))]
    password.append(currentLetter)
for x in range(0, nr_symbols):
    currentSymbol = symbols[random.randint(0, (len(symbols)-1))]
    while True:
        currentReplace = random.randint(0, totalNr)
        if currentReplace in replacedSpots:
            continue
        else:
            break
        print(currentReplace)
        print(currentSymbol)
    password[(currentReplace-1)] = currentSymbol
    replacedSpots.append(currentReplace)
for x in range(0, nr_numbers):
    currentNr = numbers[random.randint(0, (len(numbers)-1))]
    while(True):
        currentReplace = random.randint(0, totalNr)
        if currentReplace in replacedSpots:
            continue
        else:
            break
    password[(currentReplace-1)] = currentNr
    replacedSpots.append(currentReplace)
print("".join(password))
    
