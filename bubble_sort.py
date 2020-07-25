size=int(input("Enter size of list : "))
list1=[]
print("Enter elements : ")
for i in range(size):
    list1.append(int(input()))
print(f"The given list is {list1}")
for i in range(size):
    for j in range(size-i-1):
        if list1[j]>list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
print("After sorting the elements are : ",list1)