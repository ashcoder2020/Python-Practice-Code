import array as arr
list1=[]
size=int(input("Enter size of array : "))
print("Enter elements : ")
for i in range(size):
    list1.append(int(input()))

a=arr.array('i',list1)
print("You entered element is : ")
print(list(a))
while True:
    print("\nWhich operation you want to perform :")
    print("1.Print_Array\n2.Add_Element\n3.Delet_Element\n4.Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        for numbers in a:
            print(numbers,end=" ")
    elif choice==2:
        val=int(input("Enter value to add : "))
        if isinstance(val,int):
            a.append(val)
            print(f"{val} is added successfully")
        else:
            print("You not enter integer value ")
    elif choice==3:
         d=a.pop()
         print(f"the {d} element is deleted")
    elif choice==4:
        break
    else:
        print("Enter valid choice :")