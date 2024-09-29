def capitalize(s):
    splitted = s.split(" ")
    new = []

    for word in splitted:
        new.append(word.capitalize())

    capitalized = (" ".join(new))

    return capitalized

print("This program capitalizes i.e., vishesh s rajput -> Visheh S Rajput.")

s = input("\nEnter a full name: ")
capitalized = capitalize(s)

print("\n" + capitalized)
    

