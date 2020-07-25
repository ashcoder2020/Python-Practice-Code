def fib(n):
    first=0
    second=1
    for i in range(n):
        print(first,end=" ")
        temp=first
        first=second
        second=temp+second




num=int(input("Enter how long fibonacci series you want : "))
fib(num)