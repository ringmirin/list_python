marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
while i<len(marks):
   j=0
   sum=0
   ave=0
   while j<len(marks[i]):
      sum+=(marks[i][j])
      ave=sum/len(marks[i])
      j+=1
   i+=1
   print(ave)
   
      
      
#####    
      
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
i=0
while i<len(marks):
   j=0
   sum=0
   ave=0
   while j<len(marks[i]):
      sum=sum+marks[i][j]
      ave=sum/len(marks[i])
      j+=1
   i+=1
   print("Average of",i,"year",ave)