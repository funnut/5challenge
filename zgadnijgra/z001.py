# Gra w zgadywanie liczby
# Użytkownik zgaduje liczbę wylosowaną przez program w określonym zakresie (i czasie?) (np. od 1 do 100). Program podpowiada, czy liczba jest za duża, za mała czy trafiona.

# Zgadnij liczbe od 0 do 100!
# Jestes bardzo blisko!
# INPUT 69

# Witaj!
#   1. Rozpocznij gre
#   2. Wyjdz z gry
#

# Podaj login

### Generator losowych liczb
### Funkcja sprawdzajaca "odleglosc" inputu (wartosci bezwzgledne)

losowa = 50


def sprawdz_odleglosc (a, b):
	return abs(a-b)

def komentator (a):
	if a <= 5:
		return "Jestes juz bardzo blisko!"
	elif a <= 10:
		return "Blisko, blisko..."
	elif a <= 20:
		return "Bunkrow nie ma ale niedaleko"
	elif a <= 50:
		return "Kazdy miewa gorsze dni"
	elif a <= 75:
		return "Bardzo, bardzo zimno"


while True:
	strzal = int(input())
	odleglosc = sprawdz_odleglosc(losowa, strzal)

	if odleglosc:
		print (komentator(odleglosc))
	else:
		print ("Strzal w dziesiatke!")
		break
