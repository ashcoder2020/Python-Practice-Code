text=input("Enter a text : ")
list=['a','e','i','o','u','A','E','I','O','U']
vovel=[]
for i in text:
    if i in list:
        vovel.append(i)
print(vovel)
print(f"Total vovels in given text is {len(vovel)}")
