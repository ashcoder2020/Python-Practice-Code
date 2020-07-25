n=int(input("Enter size of list: "))
list=[]
print("Enter elements: ")
for i in range(n):
    list.append(input())
maxx=max(list)
print(list)
print("Maximum number is ",maxx)