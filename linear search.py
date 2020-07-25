size=int(input("Enter size how many elements you want to add in list : "))
print("Enter elements : ")
list=[]
for i in range(size):
    list.append(input())
search=int(input("Enter element you want to search in list : "))
for i in range(size):
    if int(list[i])==search:
        print("Element is found at position ",i+1)
        break
else:
    print("Element is not found in list")
