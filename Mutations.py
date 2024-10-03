print("This program mutates the immutable string!")

def mutation(string, pos, char):

    neoString = string[:pos] + char + string[pos + 1:]
    
    return neoString


string = input("\nEnter a string for mutation: ")
pos = int(input("Enter the mutating position: ")) #index
char = input("Enter the character for mutation: ")

cool = mutation(string, pos, char)

print("\n" + cool)
