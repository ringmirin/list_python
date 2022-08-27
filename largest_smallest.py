i=0
list1=[]

num=int(input("enter the number of element:"))
while i<num:
   ele=int(input("enter the element:"))
   list1.append(ele)
   i=i+1
x=0
largest=list1[0]
smallest=list1[0]
while x<len(list1):
   if list1[x]>largest:
      largest=list1[x]
   if list1[x]<smallest:
      smallest=list1[x]
   x+=1
print("largest:",largest)
print("smallest:",smallest)





      








