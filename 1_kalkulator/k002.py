# Kalkulator tekstowy
# Napisz prosty kalkulator, który wykonuje podstawowe działania matematyczne, takie jak dodawanie, odejmowanie, mnożenie i dzielenie.

### k002 ###
############

# Ta wersja ma wykonywac konkretne obliczenia na polecenie
# - pobierz x danych i zapisz
# - gdy sum, min, iloraz itd wykonaj obliczenia i zwroc wynik
# - first in first out
# - gdy break to break

# Wpisz liczbe lub polecenie:
#   [3, 4, 6]
# >> suma
# >> roznica
# >> iloczyn
# >> iloraz
### break

liczby = []

while True:
	print ('>> suma') # mozna uzyc jednego print print("""\  """)
	print ('>> roznica')
	print ('>> iloczyn')
	print ('>> iloraz')
	print ('## break')
	print (liczby)
	user_input = input("Wpisz liczbe lub polecenie: ")
	if user_input == 'suma':
		print ('Suma wynosi: ', sum(liczby))
		break
	elif user_input == 'roznica':
		roznica = liczby[0]
		for liczba in liczby[1:]: # 1: pomija liczby[0]
			roznica = roznoca - liczba
		print (roznica)		# lub od poz 0 odjac sume pozostalych wynik = liczby[n] - sum(liczby[n+1:])
		break
	elif user_input == 'iloczyn':
		iloczyn = 1
		for liczba in liczby:
			iloczyn = iloczyn * liczba # iloczyn *= liczba
		print (iloczyn)
		break
	elif user_input == 'iloraz':
		iloraz = liczby[0]
		for liczba in liczby[1:]:
			iloraz /= liczba
		print (iloraz)
		break
	else:
		liczby.append(float(user_input))

