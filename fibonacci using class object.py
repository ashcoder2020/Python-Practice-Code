class Fibinacci:
    def fib(self,n):
        first=0
        second=1
        for i in range(n):
            print(first,end=" ")
            temp=first
            first=second
            second=temp+second



if __name__ == '__main__':
    num=int(input("Enter the range upto fibonacci series you want : "))
    a=Fibinacci()
    a.fib(num)