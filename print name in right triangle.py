name=input("Enter a Name : ")
rows=len(name)
for i in range(rows+1):
    for j in range(i):
        print(name[j],end="")
    print()
