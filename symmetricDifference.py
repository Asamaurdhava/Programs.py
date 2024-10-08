print("This program works on set and prints a pre-defined symmetric difference.")

M = int(input("Enter number of digits: "))
set_1 = set(map(int, input("Enter digits: ").split()))
N = int(input("Enter number of digits: "))
set_2 = set(map(int, input("Enter the digits: ").split()))

diff_1 = set_1.difference(set_2)
diff_2 = set_2.difference(set_1)
symDiff = diff_1.union(diff_2)

print()
for i in sorted(symDiff):
    print(i)
