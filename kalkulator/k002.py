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

liczby = [10, 7, 2]


while True:
	print ('>> suma') # mozna uzyc jednego print print("""\  """)
	print ('>> roznica')
	print ('>> iloczyn')
	print ('>> iloraz')
	print ('## break')
	print (liczby)
	user_input = input("Wpisz liczbe lub polecenie: ")
	if user_input == 'suma':
		print (f'Suma wynosi: {sum(liczby)}')
		break
	elif user_input == 'roznica':
		n=0
		wynik = liczby[n] - sum(liczby[n+1:])
		print (wynik)
		break
	elif user_input == 'iloczyn':
		print ('ILOCZYN')
		break
	elif user_input == 'iloraz':
		print ('ILORAZ')
		break
	else:
		liczby.append(float(user_input))





# if user_input.lower() == 'suma': # .lower() ???
