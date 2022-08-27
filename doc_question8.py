####Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
# sample_list=['p', 'q']
# n=5
# i=0
# list=[]
# while i<len(sample_list):
#    j=1
#    while j<n:
#       list2=sample_list[i]+str(j)
#       list.append(list2)
#       j+=1
#    i+=1
# print(list)



# a = "Mummy?Papa?Brother?Sister?Uncle"
# print(a.split())
# print(a.split('?'))
# print(a.split('?',1))
# print(a.split('?',3))
# print(a.split('?',10))
# print(a.split('?',-1))


a=["a","b","c","c","d"]
b=[5,4,3,2,1]
i=0
while i<len(b):
   b.sort()
   c=a[i] + str(b[i])
   i+=1
   print(c,end=" ")




   

