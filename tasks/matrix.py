'''Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек).
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен
сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.'''

string=input()
numberi=0
numberj=0
count=0
matrix=[]
matrix2=[]
while string!='end':
    row=[int(i) for i in string.split()]
    numberj=len(row)
    matrix.append(row)
    numberi+=1
    string=input()

for row in range(numberi):
    for col in range(numberj):
        if(row==(numberi-1) and col<(numberj-1)):
            a1 = matrix[row-1][col]
            a2 = matrix[row-numberi-row][col]
            a3 = matrix[row][col-1]
            a4 = matrix[row][col+1]
        elif(col==(numberj-1) and row<(numberi-1)):
            a1 = matrix[row-1][col]
            a2 = matrix[row+1][col]
            a3 = matrix[row][col-1]
            a4 = matrix[row][col-numberj-col]
        elif (row == (numberi-1) and col == (numberj-1)):
            a1 = matrix[row-1][col]
            a2 = matrix[row-numberi-row][col]
            a3 = matrix[row][col-1]
            a4 = matrix[row][col-numberj-col]
        else:
            a1 = matrix[row-1][col]
            a2 = matrix[row+1][col]
            a3 = matrix[row][col-1]
            a4 = matrix[row][col+1]
        a=int(a1) + int(a2) + int(a3) + int(a4)
        matrix2+=[a]


for row in matrix2:
    print(row, end=' ')
    count+=1
    if(count==numberj):
        print()
        count=0

