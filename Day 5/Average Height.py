# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
numHeights = 0
totalHeight = 0

for x in student_heights:
    totalHeight += student_heights[numHeights]
    numHeights += 1
avgHeight = totalHeight / numHeights
print(round(avgHeight))
