size=int(input("Enter size of list : "))
list=[]
print("Enter elements : ")
for i in range(size):
    list.append(input())
print(list)
for i in range(size-1):
    for j in range(size-i-1):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print("Sorted list is ",list)
