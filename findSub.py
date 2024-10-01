print("This program prints out the occurence(s) of a sub-string within a string!")

def countSub(string, sub):
    count = 0

    for i in range(0, len(string) - 1):
        if sub[0] == string[i]:
            count += 1
            
    return count

string = input("\nEnter the main string: ")
sub = input("Enter the sub-string: ")

occurence = countSub(string, sub)

print(f"\nThe occurence of \'{sub}\' in \'{string}\' is {occurence}.")
