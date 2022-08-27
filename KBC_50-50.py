question_list=["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]

options_list =[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
life=[["nine","seven"],["chennai","Delhi"],["Software Engineering","counseling"]]
life_solution=[2, 2, 1]
solution_list = [3, 4, 1]

i=0
count=0
while i<len(question_list):
   print(question_list[i])
   j=0
   while j<len(options_list[i]):
      print(j+1,options_list[i][j])
      j+=1
   user=("without live line","with live line")
   print("choose your choice:")
   print("1.without live")
   print("2.with live line")
   choice=int(input("your choice:"))
   if choice==1:
      user1=int(input("enter your ans:"))
      if user1==solution_list[i]: 
         print("congrats")
   elif choice==2:
      if count==0:
         k=0
         while k<len(life[i]):
            print(k+1,life[i][k])
            k+=1
         count+=1
         user2=int(input("enter your ans:")) 
         if user2==life_solution[i]:
            print("congrats")
               
         else:
            print("wrong answer")
      else:
         print("you have used your lifeline")
         user3=int(input("enter your answer:"))
         if user3==solution_list[i]:
            print("congrats")
         else:
            print("wrong answer")
            break
   else:
      print("wrong answer")
      break
   i+=1
   
