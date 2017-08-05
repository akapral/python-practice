number=int(input())
fact=1
if number==0:
    print(1)
else:
    for i in range(1, number+1):
        fact*=i
print(fact)
