import sys

def main():
    # Считываем x
    try:
        x = float(input("Введите x: "))
    except ValueError:
        print("Ошибка: введено не число", file=sys.stderr)
        sys.exit(1)

    # Проверка диапазона
    if not (-0.5 <= x <= 0.5):
        print("Ошибка: x должен быть в диапазоне [-0.5, 0.5]", file=sys.stderr)
        sys.exit(1)

    epsilon = 1e-10
    term = 1.0          # Первый член a_0 = 1
    total_sum = term    # Начальная сумма
    k = 0               # Индекс текущего члена (a_0)
    remainder_bound = abs(term)

    # Основной цикл
    while remainder_bound > epsilon:
        # Ограничение в 1000 включенных членов
        if k >= 1000:
            print("Ошибка: не удалось достичь точности за 1000 членов", file=sys.stderr)
            sys.exit(1)
        
        # Переходим к следующему члену
        k += 1
        term *= x / k
        total_sum += term
        remainder_bound = abs(term)

    # k - это индекс последнего добавленного члена
    # Количество включенных членов = k + 1 (так как начинали с 0)
    count_terms = k + 1

    # Вывод результата
    print(f"Сумма: {total_sum:.10f}")
    print(f"Количество членов: {count_terms}")
    print(f"Оценка остатка: {remainder_bound:.2e}")

if __name__ == "__main__":
    main()