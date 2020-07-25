f = open('demo.txt','r')
lst = []
for x in f.read():
    print(x)
    if x==' ':
        pass
    elif x=='\n':
        pass
    else:
        lst.append(x)

print(lst)
f.close()





f= open('demo.txt','a')     #w to overwrite
f.write("\nhi ashu meshram")
f.close()
f = open('demo.txt','r')
print(f.read())
f.close()







f= open('ashu.txt','w')             #x to create file
f.write('ashu')
f.close()
f = open('ashu.txt','r')
print(f.read())






import os
os.remove('ashu.txt')           #remove or delet the file






import os
if os.path.exists('ram.txt'):

    os.remove("ram.txt")
else:
    print("filke not exist")


