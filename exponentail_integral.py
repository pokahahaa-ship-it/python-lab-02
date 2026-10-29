import math
import sys

if __name__ == "__main__":
    x = float(input("x (от 0.1 до 1): "))
    if not 0.1 <= x <= 1:
        print("Ошибка: требуется 0.1 <= x <= 1", file=sys.stderr)
        sys.exit(1)

    euler_gamma = 0.5772156649015329
    eps = 1e-10
    max_terms = 1000
    k = 1
    term = x
    total = term

    while abs(term) / 3 > eps:
        if k >= max_terms:
            print("Превышен предел числа членов ряда",
                  file=sys.stderr)
            sys.exit(1)

        term *= x * k / (k + 1) ** 2
        k += 1
        total += term

    result = euler_gamma + math.log(x) + total

    print(f"Ei({x}) = {result:.10f}")
    print(f"Членов ряда: {k}")
    print(f"Оценка остатка ряда: {abs(term) / 3:.3e}")