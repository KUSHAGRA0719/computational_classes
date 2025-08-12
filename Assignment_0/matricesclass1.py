# name - kushagra
# roll number-24134003
# batch-P745
# solving assigment 0 third problem


#creating matrices to save them in file later
matrix1=[[2,-3,1.4]
        ,[2.5,1,-2]
        ,[-0.8,0,3.1]]
matrix2=[[0,-1,1]
        ,[1.5,0.5,-2]
        ,[3,0,-2]]
matrix3=[[-2]
        ,[0.5]
        ,[1.5]]
matrix4=[[1]
        ,[0]
        ,[-1]]
matrix3_transpose=[[0,0,0]]#FOR D.C


#creating file for matrices


#matrix1.txt
with open("matrix1.txt","w+") as f:
    for row in matrix1:
        line=" ".join(str(x) for x in row)
        f.write(line+"\n")
#matrix2.txt
with open("matrix2.txt","w+") as f:
    for row in matrix2:
        line=" ".join(str(x) for x in row)
        f.write(line+"\n")
#matrix3.txt
with open("matrix3.txt","w+") as f:
    for row in matrix3:
        line=" ".join(str(x) for x in row)
        f.write(line+"\n")
#matrix4.txt
with open("matrix4.txt","w+") as f:
    for row in matrix4:
        line=" ".join(str(x) for x in row)
        f.write(line+"\n")

#reading files to use them for my code

#reading matrix1.txt
matrix1=[]
with open("matrix1.txt","r") as f:
    for line in f:
        row= [float(x) for x in line.strip().split()]
        matrix1.append(row)



#reading matrix2.txt
matrix2=[]
with open("matrix2.txt","r") as f:
    for line in f:
        row= [float(x) for x in line.strip().split()]
        matrix2.append(row)


#reading matrix3.txt
matrix3=[]
with open("matrix3.txt","r") as f:
    for line in f:
        row= [float(x) for x in line.strip().split()]
        matrix3.append(row)

#reading matrix4.txt
matrix4=[]
with open("matrix4.txt","r") as f:
    for line in f:
        row= [float(x) for x in line.strip().split()]
        matrix4.append(row)

#computing AB
result1=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
       for k in range(3):
           result1[i][j]+=matrix1[i][k]*matrix2[k][j]
print(f"matrix1(A)*matrix2(B)is {result1}")

#Computing BC
result2=[[0],[0],[0]]
for i in range(3):
    for j in range(1):
       for k in range(3):
           result2[i][j]+=matrix2[i][k]*matrix3[k][j]
print(f"matrix2(B)*matrix3(c){result2}")

# COMPUTING D.C
for i in range(3):
    for j in range(1):
        
        matrix3_transpose[j][i]=matrix3[i][j]

result3=[[0]]
for i in range(3):
    for k in range(1):
         result3[0][0]+=matrix4[i][k]*matrix3_transpose[k][i]
print(f"D.C is {result3}")


#SAVING ALL RESULT IN A FILE
with open("question3results.txt","w+") as f:
    f.write(f"Following are results \n AB={result1} \n D.C={result3} \n BC={result2}")






    
    

        
        



    

