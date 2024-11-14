def dating(boys: list, girls: list):
    if len(boys) != len(girls):
        print("Внимание, кто-то может остаться без пары!")
    else:
        boys.sort()
        girls.sort()
        for boy, girl in zip(boys, girls):
            print(boy + " да " + girl)
        print()


dating(["Иван", "Федор", "Василий"], ["Марья", "Дарья", "Наталья"])
dating(["Алеша", "Петр"], ["Катя", "Лена", "Соня"])
dating([], [])
