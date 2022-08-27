# Write a python program to check whether two lists are circularly identical.
n=[1,2,3,4,5,6]
m=[6,7,8,9,5]
i=0
while i<len(n):
   if n==m:
      print("yes")
      break
   else:
      print("not")
      break
i+=1

