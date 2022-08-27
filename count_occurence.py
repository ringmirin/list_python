# Occurences-is made from the word occur which means that how many times a certain character or word appears.


char_list=["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]


lis= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 


i=0
a=[]
while i<len(lis):
   j=0
   count=0
   b=[]
   while j<len(lis):
      if lis[i]==lis[j]:
         count+=1
      j+=1
   b.append(lis[i])
   b.append(count)
   if b not in a:
      a.append(b)
   i+=1
print(a,count)