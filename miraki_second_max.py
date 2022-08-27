numbers = [5, 40, 23, 7, 5, 12, 50, 10, 70]
i=0
second_max=numbers[0]
largest=numbers[0]
while i<len(numbers):
   if numbers[i]>largest:
      largest=numbers[i]
   if numbers[i]>second_max and numbers[i]!=largest:
      second_max=numbers[i]
   i+=1
print(largest)
print(second_max)


####
num=int(input("enter the number:"))
i=0
list=[]
while i<num:
   n=int(input("enter the element:"))
   list.append(n)
   i+=1
print(list)
j=0
greatest=list[0]
second_great=list[0]
while j<len(list):
   if list[j]>greatest:
      greatest==list[j]
   if list[j]>second_great and list[j]!=greatest:
      second_great=list[j]
   j+=1
print(second_great)
print(greatest)
      
      


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

