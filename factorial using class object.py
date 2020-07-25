class Factorial:
    def fact(self,n):
        fact = 1
        if n == 0 or n == 1:
            print("Factorial is 1")
        else:
            for i in range(1, n + 1):
                fact = fact * i
            print(fact)




if __name__ == '__main__':
    num=int(input("Enter number to find factorial : "))
    obj=Factorial()
    obj.fact(num)