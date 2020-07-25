size=int(input("Enter size of list : "))
lst=[]
for i in range(size):
    lst.append(int(input()))
for i in range(size):
    min=i
    for j in range(i,size):
        if lst[j]<lst[min]:
            temp=lst[j]
            lst[j]=lst[min]
            lst[min]=temp

print("Sorted list is ",lst)