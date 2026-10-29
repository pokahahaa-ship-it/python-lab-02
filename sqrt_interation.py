import math
import sys


if __name__ == "__main__":
    a = float(input("a: "))
    if not 0 <= a <= 1_000_000:
        print("Ошибка: требуется 0 <= a <= 1000000",
file=sys.stderr)
        sys.exit(1)

    eps = 1e-10
    iterations = 0

    if a == 0:
        x = 0.0
    else:
        x = max(1.0, a)
        while iterations < 1000:
            previous = x
            x = (previous + a / previous) / 2
            iterations += 1
            if abs(x - previous) <= eps:
                break
        else:
            print("Не удалось достичь условия остановки",
file=sys.stderr)
            sys.exit(1)

    reference = math.sqrt(a)
    print(f"x = {x:.12f}")
    print(f"Итераций: {iterations}")
    print(f"Отклонение от math.sqrt: {abs(x - reference):.3e}")