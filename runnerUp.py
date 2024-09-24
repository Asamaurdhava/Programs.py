print("This program finds the runner up without the implementation of built-in sort\n")

downs = int(input("Enter the scores entry: "))
print()

scores = []
count, largest = 1, 0

for i in range(downs):
    score = int(input("Enter score " + str(count) + " : "))
    scores.append(score)
    count += 1

scores.sort(reverse = True)

print("\nRunner Up score is", scores[1])
