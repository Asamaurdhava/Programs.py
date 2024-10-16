print("This program prints table of any positive integer given as an input.")

integer = int(input("Enter any positive integer: "))

for i in range(1, 11):
  print(str(integer) + " x " + str(i) + " = " + str(integer * i))
