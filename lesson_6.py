дз 5.5
from random import randint
arr=list()
X=3
Y=4
for i in range(X):
  arr.append([randint(0, 9) for x in range(Y)])
for i in range(X):
  for j in range(Y):
    print(arr[i][j], end = ' ')
  print()
s=0
for i in range(X):
  if sum([arr[i][j] for j in range(Y)])>=s:
    SUMMA=sum([arr[i][j] for j in range(Y)])
    ST=arr[i]
print(ST,SUMMA)
дз 5.6
from random import randint
n = 3
m = 4
arr = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(10, 99))
    arr.append(row)
for row in arr:
    print(' '.join(map(str, row)))
for i in range(n):
    min_value = min(arr[i])
    min_index = arr[i].index(min_value)
    if min_value % 2 == 0:
        arr[i][min_index] = 0
    else:
        arr[i][min_index] = 1
print()
for row in arr:
    print(' '.join(map(str, row)))