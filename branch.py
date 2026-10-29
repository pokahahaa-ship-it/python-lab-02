import math


if __name__ == "__main__":
    x = float(input("x: "))

    if x <= 0:
        y = 2 * x ** 2 + math.cos(x)
    elif x < 5:
        y = x + 1
    else:
        y = math.sin(2 * x) - x ** 2

    print(f"y = {y:.6f}")