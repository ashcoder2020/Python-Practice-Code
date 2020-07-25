n=input("Enter a number to check armstrong or not : ")
size=len(n)
print(size)
num=0
for i in n:
    num=num+pow(int(i),size)
print(num)
n=int(n)
if num==n:
    print("The number is armstrong")
else:
    print("The number is not armstrong")