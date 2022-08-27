####remove all the lower letter in a given string#####

n=input("enter the string:")
vowel="aeiou"
for i in n:
   if i.lower() in "aeiou":
      print('',end="")
   else:
      print(i,end="")
      