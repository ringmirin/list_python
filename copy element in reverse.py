##Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order

i=0
list1=[]
while i<10:
   num=int(input("enter  the element"))
   list1.append(num)
   i+=1
print(list1)
list2=list1.copy()
list2.reverse()
print(list2)


i=0
list=[]
num=int(input("enter the number of element:"))
while i<num:
   ele=int(input("enter the element"))
   if ele%2==0:
      list.append(ele)
   i+=1
print(list)
