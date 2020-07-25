num=int(input("Enter a number to convert octal: "))
st=0
while num>0:
    rem=str(num%8)
    num=num//8
    print(rem,end=""[::-1])

print()
num=int(input("Enter a number to convert binary: "))
st=0
while num>0:
    rem=str(num%2)
    num=num//2
    print(rem,end=""[::-1])



