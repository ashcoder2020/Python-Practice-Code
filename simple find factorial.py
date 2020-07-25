num=int(input("Enter a number which you want to find factorial : "))
fact=1
if num==0 or num==1:
    print("Factorial is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(f"factorial of {num} is {fact}")