Дз 2.1
def divide_numbers():
    try:
        X = float(input("первое"))
        Y = float(input("второе"))
        Z = X / Y
        print(f"ответ: {Z}")
    except ZeroDivisionError:
        print("ошибка")
    except ValueError:
        print("ошибка")
divide_numbers()
Дз 2.2
S = float(input("Сумма покупки "))
X = 0.35
Y = 0
G = S
if S > 20:
    Y = S * X
    G = S - Y
Y = round(Y, 2)
G = round(G, 2)
print(f"размер скидки {Y}")
print(f"Итоговая сумма {G}")
 Дз 2.3
try:
    month_number = int(input("Месяц"))

    if month_number == 1:
        print("январь зима")
    elif month_number == 2:
        print("февраль зима")
    elif month_number == 3:
        print("март весна")
    elif month_number == 4:
        print("апрель весна")
    elif month_number == 5:
        print("май весна")
    elif month_number == 6:
        print("июнь лето")
    elif month_number == 7:
        print("июль лето")
    elif month_number == 8:
        print("август лето")
    elif month_number == 9:
        print("сенятбрь осенб")
    elif month_number == 10:
        print("октябрь осень")
    elif month_number == 11:
        print("ноябрь осень")
    elif month_number == 12:
        print("декабрь зима")
    else:
        print("Ошибка")
except ValueError:
    print("Ошибка")