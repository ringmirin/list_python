num=[23,45,67,12,97,37,27,58,48]
i=0
list_length=len(num)
while i<list_length:
   if list_length%2==1:
      print(num[list_length//2])
   else:
      n=list_length//2
      print(num[n-1]+num[n])/2
   i+=1
   break

######
num=[23,45,67,12,97,37,27,58,48]
num.sort()
print(num)
length=len(num)
i=0
while i<length:
   if length%2==0:
      median1=num[length//2]
      median2=num[length//2-1]
      median=(median1-median2)/2
   else:
      median=num[length//2]
   i+=1
   print(median)
   break

