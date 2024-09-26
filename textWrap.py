print("This program performs wrapping of the input string!")

string = input("\nEnter a string: ")
width = int(input("Enter a width: "))

newString = ""

for i in range(len(string)):
    newString += string[i]
    if (i + 1) == len(string):
        break
    if ((i + 1) % width == 0):
        newString += " "

print(newString)
