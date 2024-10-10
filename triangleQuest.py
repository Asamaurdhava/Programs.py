print("This programs prints triangle according to the input digit")

digit = int(input("\nEnter a digit to print the triangle: "))

for i in range(1, digit):
    print((10**i) // 9 * i)
    
