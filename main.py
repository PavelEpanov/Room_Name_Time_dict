def main():
    room = {"CS101":3004, "CS102":4501, "CS103":6755, "CS104":1244, "CS105":1411}
    names = {"CS101":"Хайнс", "CS102":"Альварадо", "CS103":"Рич", "CS104":"Берк", "CS105":"Ли"}
    time = {"CS101":"8:00", "CS102":"9:00", "CS103":"10:00", "CS104":"11:00", "CS105":"13:00"}

    key_user = input("Введите название кабинета: ")

    print(f"Номер - {room[key_user]}; Имя - {names[key_user]}; Время - {time[key_user]}")

main()