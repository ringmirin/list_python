i=0
list1=[]
num=int(input("enter the number:"))
while i<num:
   n=int(input("enter the element:"))
   list1.append(n)
   i+=1
x=0
list2=[]
while x<len(list1):
   if x in list1:
      if x not in list2:
         list2.append(x)
   x+=1
print(list2)



##########
n=[1,2,3,4,1,2,3]
list=[]
i=0
while i<len(n):
   if i in n:
      if i not in list:
         list.append(i)
   i+=1
print(list)

