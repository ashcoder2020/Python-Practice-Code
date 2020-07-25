size=int(input("Enter size of list : "))
lst1=[]

for i in range(size):
    lst1.append(int(input()))
print("Given list is :",lst1)
pivot=lst1[0]
left_list=[]
right_list=[]
lb=lst1[0]
ub=size-1

for j in range(1,size):
    if lst1[j]>=pivot:
        left_list.append(lst1[j])
    if lst1[j]<=pivot:
        right_list.append(lst1[j])
def partition(lst1,lb,ub):
    pivot=lst1[0]
    stat=lb
    end=ub
    while(lst1[])