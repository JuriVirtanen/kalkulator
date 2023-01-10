import logging
logging.basicConfig(level=logging.INFO)

def spr_liczba(tekst):
    try:
        float(tekst)
    except:
        print("To nie jest liczba!")
        return False
    return True

while True:
    print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ", end='')
    choice = input()
    wynik = 0
    if choice == '1':
        first = input("Podaj składnik 1: ")
        if spr_liczba(first) == False:
            continue
        second = input("Podaj składnik 2: ")
        if spr_liczba(second) == False:
            continue
        logging.info(f"Dodaje {first} i {second}")
        wynik = float(first) + float(second)
        print(wynik)

    if choice == '2':
        first = input("Podaj składnik 1: ")
        if spr_liczba(first) == False:
            continue
        second = input("Podaj składnik 2: ")
        if spr_liczba(second) == False:
            continue
        logging.info(f"Odejmuje {first} i {second}")
        wynik = float(first) - float(second)
        print(wynik)

    if choice == '3':
        first = input("Podaj składnik 1: ")
        if spr_liczba(first) == False:
            continue
        second = input("Podaj składnik 2: ")
        if spr_liczba(second) == False:
            continue
        logging.info(f"Mnoże {first} i {second}")
        wynik = float(first) * float(second)
        print(wynik)

    if choice == '4':
        first = input("Podaj składnik 1: ")
        if spr_liczba(first) == False:
            continue
        second = input("Podaj składnik 2: ")
        if spr_liczba(second) == False:
            continue
        if second == '0':
            logging.info("Wracam do początku, dzielenie przez zero")
            print("Nie można dzielić przez 0")
            continue
        logging.info(f"Dziele {first} i {second}")
        wynik = float(first) / float(second)
        print(wynik)
