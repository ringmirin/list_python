   
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
x=[]
while i<len(n):
   j=0
   y=[]
   while j<len(n):
      if n[i]+n[j]==number:
         y.append(n[i])
         y.append(n[j])
         x.append(y)
      j+=1
   i+=1
print(x)
            
   
