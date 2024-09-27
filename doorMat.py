print("This program prints Door Mat of N x M configuration.")

values = input("\nEnter N & M having M 3 times of N: ")
n, m = values.split(" ")
N = int(n)
M = int(m)

hyphen = "-"
combo = ".|."

if (N % 3 != 0):
    print("N must be odd! Run the program again.")
else:
    if (N * 3) == M:
        for i in range(N):
            if i < N // 2:
                pattern = ".|." * (2 * i + 1)
            elif i == N // 2:
                pattern = "WELCOME"
            else:
                pattern = ".|." * (2 * (N - i - 1) + 1)
            print(pattern.center(M, "-"))
