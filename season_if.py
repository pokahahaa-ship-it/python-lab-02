if __name__ == "__main__":
    moth = int(input("Номер месяца: "))

    if moth == 12 or moth == 1 or moth == 2:
        print("Зима")
    elif 3 <= moth <= 5:
        print("Весна")
    elif 6 <= moth <= 8:
        print("Лето")
    elif 9 <= moth <= 11:
        print("Осень")
    else:
        print("Ошибка: номер месяца должен быть от 1 до 12")