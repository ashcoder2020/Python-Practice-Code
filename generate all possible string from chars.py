import random
list=[]
char_list = ['a','e','i','o','u']
for i in range(50):
    random.shuffle(char_list)
    a=(''.join(char_list))
    list.append(a)
print(list)