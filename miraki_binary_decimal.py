binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
decimal=0
for digit in binary_number:
   decimal=decimal*2+int(digit)
print(decimal)


binary_number = [1, 0, 0, 2, 1]
decimal=0
for digit in binary_number:
   decimal=decimal*2+int(digit)
print(decimal)

binary_number = [1, 0, 0, "1", 1]
i=0
decimal=0
while i<len(binary_number):
   decimal=decimal*2+int(binary_number[i])
   i+=1
print(decimal)
   

###

n=[1,0,0,0,0,1,1]
decimal=0
i=0
while i<len(n):
   decimal=decimal*2+n[i]
   i+=1
print(decimal)

