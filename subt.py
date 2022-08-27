list1=[1,3,2]
i=1
a=[]
while i<len(list1):
   b=list1[i]-list1[0]
   a.append(b)
   i+=1
print(a)