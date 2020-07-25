size = int(input("Enter size of list: "))
print("Enter elements :")
temp = 0
lst = [int(input()) for i in range(size)]
# Bubble sorting
for i in range(size):
    for j in range(size-i-1):
        if lst[j]>lst[j+1]:
            t=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=t
print(lst)

#selection sort
for i in range(size):
    min=i
    for j in range(i,size):
        if lst[i]>lst[min]:
            t=lst[i]
            lst[i]=lst[min]
            lst[min]=t
print(lst)





#merge sort

print(lst)
val = int(input("Enter value to search :"))
low = 0
high = size - 1
mid = (low + high) // 2
while (low <= high):
    mid = (low + high) // 2
    if lst[mid] == val:
        print("Value is found at position ", mid + 1)
        temp = 2
        break
    elif val > lst[mid]:
        low = mid + size - 1
    else:
        high = mid - 1
if temp != 2:
    print("Element not found ")
