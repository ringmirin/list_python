list=[5,10,15,20,25,50,20]
index=list.index(20)
list[index]=200
print(list)

##remove 20 ####
list=[5,20,15,20,25,50,20]

while 20 in list:
   
   list.remove(20)
print(list)

list=[5,20,15,20,25,50,20]
for i in list:
   if i==20:
      list.remove(20)
print(list)



