n1=int(input("enter the number of row and col:"))
a=[]
i=0
while i<n1:
   j=0
   b=[]
   while j<n1:
      n2=int(input("enter the number:"))
      b.append(n2)
      j+=1
   i+=1
   a.append(b)
print(a)
sum_row=0
sum_col=0
x=0
while x<len(a):
   y=0
   sum_row=sum_row+a[x][y]
   sum_col=sum_col+a[y][x]
   x+=1
print(sum_row)
print(sum_col)
c=0
d=0
# f=(len(a)-1)
d1=0
d2=0
while c<len(a):
   d1=d1+a[c][d]
   d2=d2+a[c][d]
   c+=1
   d+=1
   # f-=1
print(d1)
print(d2)
if sum_col==sum_row==d1==d2:
   print("magic square")
else:
   print("not magic square")

