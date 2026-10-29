a = float(input("Введите первое число (a): "))
b = float(input("Введите второе число (b): "))
c = float(input("Введите третье число (c): "))

if a >= b and a >= c:
    max_number = a
elif b >= a and b >= c:
    max_number = b
else:
    max_number = c

print(f"Наибольшее число: {max_number}")