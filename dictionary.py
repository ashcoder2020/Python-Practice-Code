dic = {
    'name' : 'ashu',
    'age' : 20,
    'college' : 'GHRIET'
}
print(dic)              #print all dictionary

a = dic['name']                 #get the value of key
print(a)
dic['name'] ='ashish'       #change the key value
print(dic)

x = dic.get('age')              #get the value of dictionary
print(x)

for i in dic:               #get all keys
    print(i)

for i in dic:                       #get all value in dictionary
    print(dic[i])


for x in dic.values():              #get value of dictionary
    print(x)


#get key value pair both
for i,j in dic.items():
    print("key:",i,"value:",j)


#chek key present in dictionary
if 'age' in dic:
    print("present")
else:
    print("not present")


#give length of dictionary
print(len(dic))

#add item
dic['mobile'] = 7057559583
print(dic)

#remove item
dic.pop('mobile')
print(dic)

#remove last item in dictionary
dic.popitem()
print(dic)


#clear or empty  dictionary
dic.clear()
print(dic)


#copy dictionary
dic1 = dic.copy()
print("new:",dic1)



# nested dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(myfamily['child2'])

print(myfamily['child3']['name'])
print(myfamily['child2']['name'])


for i,j in myfamily.items():
    print(i,j)

for i,j in myfamily['child1'].items():
    print(i,j)
    

myfamily['child3']['name'] = 'ashish'
print(myfamily)
