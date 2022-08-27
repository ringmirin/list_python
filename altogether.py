# count of odd numbers ….
# count of even numbers ….
# count of all the numbers ….
# sum of odd numbers ….
# sum of even numbers ….
# sum of all the numbers ….
# average of odd numbers ….
# average of even numbers ….
# average of all the numbers k


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
odd=0
even=0
total=0
i=0
while i<len(elements):
   total=len(elements)
   if elements[i]%2==0:
      even+=1
   else:
      odd+=1
   i+=1
print("odd:",odd)
print("even:",even)
i=0
sum_even=0
sum_odd=0
sum_all=0
while i<len(elements):
   if elements[i]%2==0:
      
      sum_even=sum_even+elements[i]
   else:
      sum_odd+=elements[i]
   i+=1
sum_all=sum_even+sum_odd
print("sum of even:",sum_even)
print("sum of odd:",sum_odd)
print("sum of all:",sum_all)
i=0
ave_even=0
ave_odd=0
ave_all=0
while i<len(elements):
   ave_even=sum_even/even
   ave_odd=sum_even/odd
   i+=1
ave_all=ave_even+ave_odd
print("avearge of even:",ave_even)
print("average of odd:",ave_odd)
print("average of all:",ave_all)
   


      

   
   