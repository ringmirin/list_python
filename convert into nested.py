n=[1,2,3,4,5,6,7,8,9]
i=0
m=[]
while i<len(n):
   k=n[i:i+2]
   m.append(k)
   i+=2
print(m)