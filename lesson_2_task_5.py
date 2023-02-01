def month_to_season(i):
    if (i<1 or i>12):
        print("Введите правильный номер месяца")
    else:
        if (i>11 or i<3):
            print("Зима")
        else:
            if (i>2 and i<6):
                print("Весна")
            else:
                if (i>5 and i<9):
                    print("Лето")
                else:
                    if (i>8 and i<12):
                        print("Осень")

month_to_season(13)

