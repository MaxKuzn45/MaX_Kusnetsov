дз 3.1
try:
    n = int(input("число"))
    if 1 <= n <= 100:
        s = sum(i ** 3 for i in range(1, n + 1))
        print(f"Сумма = {s}")
    else:
        print("Ошибка")
except ValueError:
    print("Ошибка")
дз 3.2
for sh in range(1, 11):
    for dl in range(1, 11):
        print('{:2d}'.format(dl*sh), end=' ')
    print(' ')