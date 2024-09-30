import math

print("This program calculates and prints the angle (in degrees) formed by two sides of a right-angled triangle, given the lengths of those sides as user input1.\n")

AB = int(input("Enter length of AB: ")) #lengths are out of natural numbers
BC = int(input("Enter length of BC: ")) #lengths are out of natural numbers

tan_theta_radians = math.atan2(AB, BC)

degree_theta = math.degrees(tan_theta_radians)

if (degree_theta > 0) and (degree_theta < 90):
    angle = round(degree_theta)

print("\n" + str(angle) + chr(176))
