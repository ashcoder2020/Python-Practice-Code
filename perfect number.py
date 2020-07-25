num=int(input("Enter a number to check perfect number : "))
list=[]
for i in range(1,num):
    if num%i==0:
        list.append(i)

if sum(list)==num:
    print("The number is perfect number ")
else:
    print("The number is not a perfect number")

