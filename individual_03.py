for bulls in range(11):
    for cows in range(21):
        calves = 100 - bulls - cows
        if calves >= 0 and (20 * bulls + 10 * cows + calves) == 200:
            print(f"Быки: {bulls}, Коровы: {cows}, Телята: {calves}")