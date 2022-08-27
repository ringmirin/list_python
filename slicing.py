# 12.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.  
sample_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del sample_list[4:]
del sample_list[0]
print(sample_list)



##########
sample_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
i=0
while i<len(sample_list):
      del sample_list[4:]
      del sample_list[0]
      print(sample_list)
      break
i+=1
      