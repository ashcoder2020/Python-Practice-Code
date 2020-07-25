
#arithmatic operation using lambda function
a,b=map(int,input("Enter two numbaers : ").split())
add = lambda a,b: a + b
sub = lambda a,b: a - b
mul = lambda a,b: a * b
div = lambda a,b: a / b
print("addition is ",add(a,b))
print("substraction is ",sub(a,b))
print("multiplication is ",mul(a,b))
print("Division is ",div(a,b))




#Square root of a number
num = int(input("Enter number:"))
num_sqrt = num ** 0.5
print('The square root is:',num**0.5)



#swap two numbers
a,b = 10,20
a,b=b,a
print("a",a,"and b",b)




#find quadratic equation
import cmath
a,b,c = 1,4,5
# calculate delta
d = (b**2) - (4*a*c)            #b**2-4ac
#  two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))




#generate random number
import random
print(random.randint(0,444))




