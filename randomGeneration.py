import random, time

print("This program prints randomly generated number that are even and less than 100\n")

randomNum = random.randint(1, 100)

'''for i in range(1, 101):
    print(randomNum)
    time.sleep(0.1)
    randomNum = random.randint(1, 100)'''

if (randomNum % 2) == 0:
    print("There's an even number, and it is...")
    time.sleep(3)
    print(randomNum, "\n")