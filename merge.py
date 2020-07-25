lst=[]
size=int(input("Enter size of list : "))
print("Enter elements : ")
for i in range(size):
    lst.append(int(input()))
print(lst)

def merge(a,b):
    c=[]
    i,j=0,0
    while i<len(a) and j<len(b):
        while a[i] <b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            b+=1

    if i==len(a):
        c.extend(b[j])
    else:
        c.extend(a[i])
    print(c)

def mergesort(a):
    left=mergesort(a[:len(a)//2])
    right=mergesort(a[len(a)//2:])
    return merge(left,right)
mergesort(lst)
