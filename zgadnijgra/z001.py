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

losowa = 91


print ("Podaj nazwe gracza: ")
username = str(input())
print (f"Witaj {username}!\nWlasnie jedna z liczb w przedziale od 0 do 100 sie zgubila...\nCzy potrafisz ja odnalezc?\nPodaj jaka to liczba: ")

while True:
	try:
		strzal = int(input())
		odleglosc = funk.sprawdz_odleglosc(losowa, strzal)

		if odleglosc:
			print (funk.komentator(odleglosc))
		else:
			print (f"Strzal w dziesiatke!\nChodzilo o liczbe {losowa}")
			break

	except ValueError:
		print ("Szukamy liczby calkowitej!")
