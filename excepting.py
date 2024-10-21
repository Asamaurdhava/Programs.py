print("This program test the knowledge of exceptions.")

T = int(input("\nEnter number of test cases: "))

for i in range(1, T + 1):
    try:
        a, b = input(f"\nTest case {i}: ").split()
        quotient = int(a) // int(b)
        print(quotient)
    except ZeroDivisionError as ZDE:
        print("Error Code:", ZDE)
    except ValueError as VE:
        print("Error Code:", VE)
    except Exception as e:
        print("Error Code:", e)
    
