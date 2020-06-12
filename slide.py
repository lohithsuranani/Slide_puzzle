import random
n = int(input('n where nxn is the size of puzzle:'))
list1=[]
for i in range(0,n*n):
    list1.append(i)
random.shuffle(list1)

matrix = []
while list1 !=[]:
    matrix.append(list1[:n])
    list1 = list1[n:]
for i in matrix:
    for j in i:
        print(j,end="\t")
    print('\n')