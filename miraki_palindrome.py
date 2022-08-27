name=[ 'n', 'i', 't', 'i', 'n' ]
rev=reversed(name)
if list(name)==list(rev):
   print("palindrome")
else:
   print("not")


string=input(("enter the letter"))
if string==string[::-1]:
   print("palindrome")
else:
   print("not")

###
name=[ 'n', 'o', 't', 'i', 'n' ]
if name==name[::-1]:
   print("palindrome")
else:
   print("not")




####
a=[2,3,15,11,3,2]
i=0
while i<len(a):
   if a==a[::-1]:
      print("yes")
      break
   else:
      print("not")
      break


####
list1=[1,2,3,4,5,6]
list2=[2,3,4,0,5,7]
list3=[item for item in list1 if item not in list2]
print(list3)

####
n=[30,40,28,16,39,50,59,48]
total=0
index=0
while index<len(n):
   total=total+n[index]
   index+=1
print(total)