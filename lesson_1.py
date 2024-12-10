#дз 1.1
import math
R = float(input("радиус: "))
L = 2 * math.pi * R
S = math.pi * (R ** 2)
L_rounded = round(L, 2)
S_rounded = round(S, 2)
print(f"L: {L_rounded} см")
print(f"S: {S_rounded} см²")
#дз 1.2
x = 10
y = 55
print("до:")
print(f"x = {x}")
print(f"y = {y}")
x, y = y, x
print("после:")
print(f"x = {x}")
print(f"y = {y}")
#дз 1.3
import math
g = 9.81
L = float(input("Длина маятника "))
T = 2 * math.pi * math.sqrt(L / g)
print(f"Период колебания: {T:.2f} с")
