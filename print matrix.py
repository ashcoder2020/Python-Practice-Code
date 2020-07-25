import array as arr
list1=[]
row,clm=map(int,input("Enter row and column : ").split())
print("Enter elements : ")
for i in range(row):
    for i in range(clm):
        list1.append(input())


print("The inputed array is :")
for i in range(row):
    for j in range(clm):
        print(list1,end=" ")
    print()
