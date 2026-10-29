import math
import sys

if __name__ == "__main__":
    n = int(input("n: "))
    x = float(input("x: "))

    if not (0 <= n <= 10000 and 0 < x <= 100):
        print("Ошибка: требуется 0 <= n <= 10000 и 0 < x <= 100",
              file=sys.stderr)
        sys.exit(1)

    total = 0.0
    for k in range(1, n + 1):
        term = math.log(k * x) / k ** 2
        total += term

    print(f"S = {total:.6f}")