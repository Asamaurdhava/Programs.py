print("This program has No Idea!")

values = input("\nEnter space-separated values: ")
myList = list(map(int, input("Enter digits: ").split()))
set_1 = set(map(int, input("Enter the digits: ").split()))
set_2 = set(map(int, input("Enter digits: ").split()))

happiness = 0

for i in myList:
    if i in set_1:
        happiness += 1
    if i in set_2:
        happiness -= 1

print("\nHappiness: ", happiness)
