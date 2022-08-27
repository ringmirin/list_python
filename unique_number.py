list=[1,2,3,3,5,7,4,4,2]
i=0
a=[]
count=0
while i<len(list):
   if list[i] not in a:
      a.append(list[i])
      count+=1
   i+=1
print(a)
print(count)


