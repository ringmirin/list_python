magic_square = [
[8, 3, 4],
[1, 5, 9],
[6, 7, 2]
]
sum_row=0
sum_col=0
i=0
while i<len(magic_square):
   j=0
   sum_row=sum_row+magic_square[i][j]
   sum_col=sum_col+magic_square[j][i]
   i+=1
# print(sum_row)
# print(sum_col)
if sum_row==sum_col:
   print("magic_square")
else:
   print("not magic square")
   
   ###############     #########
   
magic_square = [
[5, 3, 7],
[1, 8, 9],
[6, 4, 2]
]
col=0
row=0
i=0
while i<len(magic_square):
   j=0
   col=col+magic_square[i][j]
   row=row+magic_square[j][i]
   i+=1
if col==row:
   print("magic square")
else:
   print("not magic square")
   
 



