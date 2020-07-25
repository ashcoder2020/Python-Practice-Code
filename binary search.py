n=int(input("Enter How many elements you want to add in list : "))
list=[]
print("Enter elements : ")
for i in range(n):
    list.append(input())
list.sort()
print(list)
svalue=int(input("Enter value which you want to search in list : "))
start=0
end=n-1
def search(list,start,end):
    while start<end:
        for i in range(n):
            mid=(start+end)//2
            if svalue==mid:
                print("The value is found at position ",i+1)
                break

            elif svalue<mid:
                end=mid-1

            elif svalue>mid:
                start=mid+1

        else:
            print("The value is not found")
print(search(list,start,end))
