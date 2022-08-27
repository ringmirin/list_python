# Write a program to find the sum of all elements of a list.

i=0
list=[]
sum=0
while i<5:
   num=int(input("enter the element"))
   list.append(num)
   sum=sum+list[i]
   i+=1
   
   
print(sum)



