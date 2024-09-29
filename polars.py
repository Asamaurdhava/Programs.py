print("This program converts a complex number to polar coordinate.")

from cmath import polar

cNum = complex(input("\nEnter a complex number: "))

r, phi = polar(cNum)

print()
print(round(r, 15))
print(round(phi, 17))
