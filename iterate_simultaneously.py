list1=[10,20,30,40,50,60,70]
list2=[100,200,300,400,500,600,700]
for x,y in zip(list1,list2[::-1]):
   print(x,y)
   



#####
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
i=0
while i<len(students):
   a=students[i]+str(marks[i])
   i+=1
   print(a)



