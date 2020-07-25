size=int(input("Enter a number to check prime or not:"))
for i in range(2,size):
    if size%i==0:
        print("prime")
        break
else:
    print("Not prime")

