question_list=[
"How many continents are there?",
"What is the capital of India?",
"NG mei kaun se course padhaya jaata hai?"]

options_list =[
["Four", "Nine", "Seven", "Eight"],

["Chandigarh", "Bhopal", "Chennai", "Delhi"],

["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1]
i=0
j=0
while i<len(question_list) and j<len(options_list):
   print(i+1,question_list[i])
   k=0
   while k<len(options_list[j]):
      print(k+1,options_list[j][k])
      k+=1
   sol=int(input("Enter your solution:"))
   if sol==solution_list[i]:
      print("CONGRATULATIONS")
   else:
      print("WRONG ANSWER")
   i+=1
   j+=1


         
      


   






















