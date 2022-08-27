student_marks=[23,45,89,90,56,80]
length=len(student_marks)
index=0
total=0
while index<length:
   total=student_marks[index]+total
   index+=1
   print ("total_marks:"+str(total))


####
student_marks=[23,45,67,89,90,54,34,21,34,23,19]
list_length=len(student_marks)
index=0
less_than50=0
more_than50=0
while index<list_length:
   marks=student_marks[index]
   if marks<50:
      less_than50=less_than50+1
   else:
      more_than50=more_than50+1
   index=index+1
print("less than50:",less_than50)
print("more than 50:",more_than50)



   
