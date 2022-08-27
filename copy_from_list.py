##Take 10 integer inputs from user and store them in a list. Now, copy all the 
# elements in another list but in reverse order

#
i=0
list1=[]
n=int(input("enter the number: "))
while i<=n:
   num=int(input("enter the element: "))
   list1.append(num)
   i+=1
print("list1:",list1)
list2=list1
print("list2:",list2)
