# Write a Python program to compute the difference between two lists.


data1=["red", "orange", "green", "blue", "white"]
data2=["black", "yellow", "green", "blue"]
color1=[item for item in data1 if item not in data2]
color2=[item for item in data2 if item not in data1]
print(color1)
print(color2)

   





   

