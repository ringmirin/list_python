# Write a Python program to find the list in a list of lists whose sum of elements is the highest.



list=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
i=0
total=0
index=0
while i<len(list):
   j=0
   sum=0
   while j<len(list[i]):
      sum=sum+(list[i][j])
      j+=1
   if sum>total:
      total=sum
   i+=1
print(total)


### 
num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
index = 0
max_index = 0
sum_max = 0
for list in num:
   sum_list = 0
   for x in list:
      sum_list += x
   if sum_list > sum_max:
      sum_max = sum_list
      max_index = index
   index += 1
print(num[max_index])  