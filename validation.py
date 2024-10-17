print("This program takes input if the entered text is devoid of numericals.\n")

text = input("Enter a text for input: ")

numericals = False

for i in range(0, 10):
    if str(i) in text:
        numericals = True
        print("\nCan't take input as it contains numericals.")
        break
    else:
        print("\nCan take input inside.")
        break
