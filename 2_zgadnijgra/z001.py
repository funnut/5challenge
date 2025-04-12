# Gra w zgadywanie liczby
# Użytkownik zgaduje liczbę wylosowaną przez program w określonym zakresie (i czasie?) (np. od 1 do 100). Program podpowiada, czy liczba jest za duża, za mała czy trafiona.

# Zgadnij liczbe od 0 do 100!
# Jestes bardzo blisko!
# INPUT 69

# Witaj!
#   1. Rozpocznij gre
#   2. Wyjdz z gry

# Podaj login

### Generator losowych liczb
### Funkcja sprawdzajaca "odleglosc" inputu (wartosci bezwzgledne)

from random import randrange
import readline
import math
import os


def wczytaj_najlepsza_celnosc():
    if os.path.exists('/data/data/com.termux/files/home/kod/5challenge/2_zgadnijgra/najlepsza_celnosc.txt'):
        with open('/data/data/com.termux/files/home/kod/5challenge/2_zgadnijgra/najlepsza_celnosc.txt', 'r') as f:
            try:
                return float(f.read().strip())  # Odczytuje celność jako float
            except ValueError:
                return 0  # Jeśli plik jest pusty lub niepoprawny, zwróć 0
    return 0  # Jeśli plik nie istnieje, zwróć 0

def zapisz_najlepsza_celnosc(celnosc):
    with open('/data/data/com.termux/files/home/kod/5challenge/2_zgadnijgra/najlepsza_celnosc.txt', 'w') as f:
        f.write(str(celnosc))

print("\nPodaj nazwę gracza: ")
username = input().strip()  # strip usuwa spacje

print(f"""
💐🌻🌺 >>> Witaj {username}! <<< 🌻🌺🌼
\nWłaśnie jedna z liczb w przedziale od 0 do 100 się zgubiła...
\nCzy potrafisz ją odnaleźć?""")


def sprawdz_odleglosc(a, b):
    return abs(a - b)


def komentator(a):
    if a <= 2:
        return "GORACOO!"
    elif a <= 5:
        return "Bardzo blisko!"
    elif a <= 10:
        return "Blisko, blisko..."
    elif a <= 20:
        return "Bunkrów nie ma, ale niedaleko"
    elif a <= 50:
        return "Każdy miewa gorsze dni"
    elif a <= 75:
        return "Bardzo zimno"
    else:
        return "Bardzo, bardzo daleko"


# Celność = (1 / D) * log(N + 1)
# D = (abs(S₁ - L) + abs(S₂ - L) + ... + abs(Sₙ - L)) / N

def oblicz_celnosc(D, N, k=0.1):
    if D == 0:
        return 100  # Jeśli odległość jest 0, celność to 100%
    return 100 * (1 / (1 + D)) * (1 - math.exp(-k / N))


najlepsza_celnosc = wczytaj_najlepsza_celnosc()

while True:
    try:
        losowa = randrange(1, 100)
        N = 0
        D = 0
        while True:
            try:
                readline.set_history_length(100)
                strzal = int(input("\nPodaj, jaka to liczba: "))
                odleglosc = sprawdz_odleglosc(losowa, strzal)
                N += 1
                D = round((D * (N - 1) + odleglosc) / N, 2)  # Aktualizacja średniej odległości
                celnosc = oblicz_celnosc(D, N, k=0.1)
                if odleglosc:
                    print(komentator(odleglosc))
                else:
                    print(f"Strzał w dziesiątkę!\n\nChodziło o liczbę {losowa}! 👑")
                    print(f"Ilość prób: {N}")
                    print(f"Średnia odległość: {D}")
                    print(f"Celność: {celnosc:.2f}%")
                    print(f"\nNajlepsza celność z poprzednich gier: {najlepsza_celnosc:.2f}%")
                    if celnosc < 100 and celnosc > najlepsza_celnosc:
                        najlepsza_celnosc = celnosc
                        zapisz_najlepsza_celnosc(najlepsza_celnosc)  # Zapisanie najlepszej celności do pliku
                        print ("\n🎉 Nowa najlepsza celność!")
                    break
            except ValueError:
                print("Szukamy liczby całkowitej!")
        yesno = input("\nCzy chcesz zagrać ponownie? (t/n): ").lower()
        if yesno not in ['tak', 't', '']:
            print('')
            break
    except EOFError:
        print ('\n')
        yesno = []
        break
