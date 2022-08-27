# marks =[[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# i=0
# sum=0
# while i<len(marks):
#    j=0
#    total=0
#    while j<len(marks[i]):
#       total=total+marks[i][j]
#       j+=1
#    sum=sum+total
#    i+=1
# print(sum)

# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
# i=0
# total=0
# while i<len(marks):
#    j=0
#    sum=0
#    while j<len(marks[i]):
#       sum+=marks[i][j]
#       j+=1
#    total+=sum
#    i+=1
# print(total)

######
# marks =[[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# sum=0
# flatten_marks=[mark for sublist in marks for mark in sublist]
# i=0
# while i<len(flatten_marks):
#    sum=sum+flatten_marks[i]
#    i+=1
# print(sum)