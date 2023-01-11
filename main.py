import logging
logging.basicConfig(level=logging.INFO)

def spr_liczba(tekst):
    try:
        float(tekst)
    except ValueError: # coś takiego? czy chodzi o wyłapanie konkretnych errorów?
        print("To nie jest liczba!")
        return False
    return True


if __name__ == "__main__":
    while True:
        choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
        wynik = 0
        if choice == '1':
            first = input("Podaj składnik 1: ")
            if not spr_liczba(first):
                continue
            second = input("Podaj składnik 2: ")
            if not spr_liczba(second):
                continue
            logging.info(f"Dodaje {first} i {second}")
            wynik = float(first) + float(second)

        elif choice == '2':
            first = input("Podaj składnik 1: ")
            if not spr_liczba(first):
                continue
            second = input("Podaj składnik 2: ")
            if not spr_liczba(second):
                continue
            logging.info(f"Odejmuje {first} i {second}")
            wynik = float(first) - float(second)

        elif choice == '3':
            first = input("Podaj składnik 1: ")
            if not spr_liczba(first):
                continue
            second = input("Podaj składnik 2: ")
            if not spr_liczba(second):
                continue
            logging.info(f"Mnoże {first} i {second}")
            wynik = float(first) * float(second)

        elif choice == '4':
            first = input("Podaj składnik 1: ")
            if not spr_liczba(first):
                continue
            second = input("Podaj składnik 2: ")
            if not spr_liczba(second):
                continue
            if second == '0':
                logging.info("Wracam do początku, dzielenie przez zero")
                print("Nie można dzielić przez 0")
                continue
            logging.info(f"Dziele {first} i {second}")
            wynik = float(first) / float(second)

        else:
            break
        print(wynik)