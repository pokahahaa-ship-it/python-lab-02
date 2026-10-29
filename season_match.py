if __name__ == "__main__":
    month = int(input("Номер месяца: "))

    match month:
        case 12 | 1 | 2:
            print("Зима")
        case 3 | 4 | 5:
            print("Весна")
        case 6 | 7 | 8:
            print("Лето")
        case 9 | 10 | 11:
            print("Осень")
        case _:
            print("Ошибка: номер месяца должен быть от 1 до 12")