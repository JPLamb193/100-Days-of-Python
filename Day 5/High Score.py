# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highestScore = 0
index = 0
for x in student_scores:
    if student_scores[index] > highestScore:
        highestScore = student_scores[index]
    index += 1
print(f"The highest score in the class is {highestScore}")
