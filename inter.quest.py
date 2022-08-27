list=["11","33","50"]
str=" "
i=0
while i<len(list):
    str=str+list[i]
    i+=1
print(int(str),end=" ")

print(type(int(str)))


##############
list=[11,33,50]
list1=[str(list)for list in list]
i=0
while i<len(list):
   list2=list1[i][0:]
   i+=1
   print(list2,end="")
print(type(int(list2)))


############
list1=[1,2,3,4,5]
str1=[str(list1)for list1 in list1]                                                                                   
str="emp"
i=0
while i<len(list1):
   str2=str+str1[i]
   
   i+=1
   print(str2,end=" ")



####

list1=[1,2,3,4,5]
str1="emp" 
list3=[]
i=0
while i<len(list1):
   list=str1+str(list1[i])
   list3.append(str(list))
   i+=1
print(list3)
   
   




