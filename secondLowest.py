print("This program find the second lowest out of the entered scores and prints the recepient student's name")

entries = int(input("\nEnter the number of records to be installed: "))

big, names, scores, secondLowest = [], [], [], 0

for i in range(entries):
    student = []
    name = input("\nEnter name: ")
    score = float(input("Enter " + name + "'s score: "))
    student.append(name), student.append(score)
    big.append(student)

for j in range(len(big)):
    names.append(big[j][0])
    scores.append(big[j][1])

names.sort()
unique = set(scores)
scores = list(unique)
scores.sort()

secondLowest = scores[1]

final = []

for k in range(len(big)):
    if big[k][1] == secondLowest:
        final.append(big[k][0])

final.sort()

print("\n", final)


