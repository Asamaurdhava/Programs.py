print("The program prints the entered string reversed.\n")

aWord = input("Enter any word: ")
print()

high = len(aWord) - 1

for i in range(0, len(aWord)):
    print(aWord[high - i], end = "")

