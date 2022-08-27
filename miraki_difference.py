list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
list3=[]
for item in list1:
   if item not in list2:
      list3.append(item)
print(list3)

list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
list3=[item for item in list1 if item not in list2]
print(list3)


###

n=[10,11,12,13,14,17,18,19]
i=0
while i<len(n):
   print(n[i])
   i=i+1
   
   
####

li = ['The','quick','brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
ln= ' '.join(li)
print(ln)

