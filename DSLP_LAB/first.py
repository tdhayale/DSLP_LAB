
rows=int(input("Enter numbers of rows:"))
columns=int(input(f"Enter numbers of columns:"))

matrix =[]
for i  in range(rows):
    row=[]
    for j in range(columns):
        value=int(input(f"Enter element[{i}][{j}]:"))
        row.append(value)
    matrix.append(row)    
    
print("The matrix is:")   
for row in matrix:
    for value in row:
        print(value,end=" ")
    print()    
          
   
     
    