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



losowa = randrange(1, 100)

print ("\nPodaj nazwę gracza: ")
username = input().strip()   # strip usuwa spacje


print (f"""
>>> Witaj {username}! <<<
\nWłasnie jedna z liczb w przedziale od 0 do 100 się zgubiła...
\nCzy potrafisz ją odnaleźć?""")


def sprawdz_odleglosc (a, b):
    return abs(a-b)

def komentator (a):
    if a <= 2:
        return "GORACOO!"
    elif a <= 5:
        return "Bardzo blisko!"
    elif a <= 10:
        return "Blisko, blisko..."
    elif a <= 20:
        return "Bunkrow nie ma ale niedaleko"
    elif a <= 50:
        return "Kazdy miewa gorsze dni"
    elif a <= 75:
        return "Bardzo zimno"
    else:
        return "Bardzo, bardzo daleko"


# Główna pętla


while True:
    try:
        strzal = int(input("\nPodaj, jaka to liczba: "))
        odleglosc = sprawdz_odleglosc(losowa, strzal)
        if odleglosc: 	# Komentarz do odległości
            print (komentator(odleglosc))
        else:
            print (f"Strzal w dziesiatke!\n\nChodzilo o liczbe {losowa}!\n")
            yesno = input("\nCzy chcesz zagrać ponownie? (t/n): ")
            if yesno in ['tak','t','']:
                losowa = randrange(1, 100)
                continue
            else:
                print ('')
                break
    except ValueError:
        print ("Szukamy liczby calkowitej!")


