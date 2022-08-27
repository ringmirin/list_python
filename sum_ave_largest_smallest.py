i=0
list1=[]
num=int(input("enter the number of element in list:"))
while i<num:
   ele=int(input("enter the element:"))
   list1.append(ele)
   i+=1

x=0
sum=0
ave=0
largest=list1[0]
smallest=list1[0]
while x<len(list1):
   sum=sum+list1[x]
   ave=sum/len(list1)
   x+=1
y=0
largest=list1[0]
smallest=list1[0]
while y<len(list1):
   if list1[y]>largest:
      largest=list1[y]
   if list1[y]<smallest:
      smallest=list1[y]

   y+=1
print("sum:",sum)
print("average",ave)
print("largest is:",largest)
print("smallest is:",smallest)
