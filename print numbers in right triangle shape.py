rows=int(input("Enter How many rows you want : "))
for i in range(1,rows+1):
    for j in range(i):
        print(i,end="")
    print()


rows=int(input("Enter How many rows you want : "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print()


rows=int(input("Enter number of rows : "))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if j==1 or i==rows or i==j:
            print("*",end="")
        else:
            print(end=" ")

    print()