n=int(input("Enter a number you want upto fibonacci series: "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    temp=a
    a=b
    b=temp+b