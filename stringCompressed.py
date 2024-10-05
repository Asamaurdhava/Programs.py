print("This program compresses the given string, like a group-by.")

from itertools import groupby

S = input("\nEnter a string made up of digits (0-9): ")

compressed = ''

for char, group in groupby(S):
    count = len(list(group))
    compressed += f"({count}, {char}) "

print("\n" + compressed.strip() + "\n")

