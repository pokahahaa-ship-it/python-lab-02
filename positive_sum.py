if __name__ == "__main__":
    total = 0
    while True:
        number = int(input("Число (0 - завершить): "))
        if number == 0:
            break
        if number < 0:
            continue
        total += number

    print(f"Сумма положительных чисел: {total}")