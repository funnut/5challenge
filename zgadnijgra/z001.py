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

import funk

losowa = 50

while True:
	strzal = int(input())
	odleglosc = funk.sprawdz_odleglosc(losowa, strzal)

	if odleglosc:
		print (funk.komentator(odleglosc))
	else:
		print ("Strzal w dziesiatke!")
		break
