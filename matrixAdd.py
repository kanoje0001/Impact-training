r = int(input("Enter the number of rows in matrix 1 :- "))
c = int(input("Enter the number of columns in matrix 1 :- "))
mat = []
r1 = int(input("Enter the number of rows in matrix 2 :- "))
c1 = int(input("Enter the number of columns in matrix 2 :- "))
mat1 = []
result1 =[]
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    mat.append(row) 
print("The element of matrix 1 are :-")    
print(mat)    
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    mat1.append(row)  
print("The element of matrix 2 are :-")       
print(mat1)    
result = [[mat[i][j] + mat1[i][j]  for j in range
(len(mat[0]))] for i in range(len(mat))
result1.append(result)]
print[result]