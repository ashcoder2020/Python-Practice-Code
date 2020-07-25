size=int(input("Enter size of list : "))
lst=[]
for i in range(size):
    lst.append(int(input()))
print("Given list is ",lst)
for i in range(size):
    minpos=i
    for j in range(i,size):
        if lst[j]<lst[minpos]:
            temp=lst[j]
            lst[j]=lst[minpos]
            lst[minpos]=temp
print("Sorted list is ",lst)
