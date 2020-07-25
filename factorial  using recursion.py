def recur_factorial(n):
   if n == 1 or n==0:
       return 1
   else:
       return n*recur_factorial(n-1)

num = int(input("Enter a number: "))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   print("The factorial of",num,"is",recur_factorial(num))