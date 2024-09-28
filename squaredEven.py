print("This programs prints even squares till any entered upper limit.\n")

upperLimit = int(input("Enter any number: "))
print()

print("The list goes...")
for i in range(1, upperLimit + 1):
    squared = i * i
    if (squared % 2) == 0:
        print(squared)
