char=input("Enter a charcter :")
if char.isnumeric():
    print("It is number")
elif char.islower():
    print("It is lowercase")
else:
    print("It is uppercase")