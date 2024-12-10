#номер 1
x1, y1, z1, x2, y2, z2 = map(int, input(). split())
def find(x1, y1, z1, x2, y2, z2):
    min = 1000
    a, b, c = abs(x2 / x1), abs(y2 / y1), abs(z2 / z1)
    X = [a, b, c]
    for i in X:
        if i < min:
            min = i
    if min == a:
        print(x1, x2)
    elif min == b:
        print(y1, y2)
    else:
        print(z1, z2)
find(x1, x2, y1, y2, z1, z2)
#номер 2
n = int(input())
def dvojka(n):
    a = 2
    while a * a <= n and n % a != 0:
        a += 1
    return a * a > n
def palindrome(r):
    r = str(r)
    return r == r[::-1]
for i in range (1, n + 1):
    if dvojka(i) and palindrome(i):
        print(i)
