def recursive_pow(num, power):
    if power == 0:
        return 1
    else:
        return num * recursive_pow(num, power - 1)

num = int(input("Enter a number: "))
power = int(input("Enter it's power (x^n): "))
powered = recursive_pow(num, power)
print(str(num) + " powered " + str(power) + " is " + str(powered))
