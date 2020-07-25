num=1
for i in range(4):
    for j in range(4):
        print(num,end=" ")
        num+=1
    print()

print()
print()

for i in range(5):
    for j in range(i):
        if ((i+j) %2)==0:
            print("1",end=" ")
        else:
            print("0", end=" ")
    print()


print()
print()


for i in range(4):
    for j in range(4):
        if i<j or i>j:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
print()
print()


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print()
print()

for i in range(5):
    for j in range(i):
        print(i,end=" ")
    print()

print()
print()

for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()

print()
print()
for i in range(4):
    for j in range(4):
        for k in range(4):
            print("HI",end=" ")
        print()
    print()
print()
print()
print()

