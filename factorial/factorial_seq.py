number=int(input())
for j in range(0, number+1):
    fact=1
    for i in range(1, j+1):
        if j==0:
            print(1)
        else:
            fact*=i
    print(str(j) + " = " + str(fact))
