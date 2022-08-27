# Write a Python program to convert a list of multiple integers into a single integer. 

sample_list=[11, 33, 50]
for i in sample_list:
   print(i,end="")

sample_list=[11, 33, 50]
i=0
while i<len(sample_list):
   complex=[str(sample_list)for sample_list in sample_list]
   com="".join(complex)
   i=i+1
print(com)


## Write a Python program to compute the difference between two lists.


sample_data=["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]

colour1=[item for item in sample_data[0] if item not in sample_data[1]]
colour2=[item for item in sample_data[1] if item not in sample_data[0]]
print(colour1)
print(colour2)


