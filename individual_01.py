n = int(input())

if n == 0:
    print("Я купил 0 карандашей")
elif n == 1:
    print("Я купил 1 карандаш")
elif 2 <= n <= 4:
    print(f"Я купил {n} карандаша")
else:
    print(f"Я купил {n} карандашей")