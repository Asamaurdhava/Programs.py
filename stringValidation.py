print("This programs examines the input string against several validations!")

s = input("\nEnter any string: ")

has_alnum = False
has_alpha = False
has_digit = False
has_lower = False
has_upper = False

for char in s:
    if char.isalnum():
        has_alnum = True
    if char.isalpha():
        has_alpha = True
    if char.isdigit():
        has_digit = True
    if char.islower():
        has_lower = True
    if char.isupper():
        has_upper = True

print()
print(has_alnum)
print(has_alpha)
print(has_digit)
print(has_lower)
print(has_upper)

