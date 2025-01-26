### k002slim ###
################

liczby = []

while True:
	print ("""
\n
>> suma
>> roznica
>> iloczyn
>> iloraz
## break
""")
	print (liczby)
	user_input = input('Wpisz liczbe lub polecenie: ')
		### input check
	if user_input == 'suma':
		if liczby: # sprawdza czy lista jest True
			print ('Suma wynosi: ', sum(liczby))
			break
		else:
			print ('Lista jest pusta!')
	elif user_input == 'roznica':
		if len(liczby) > 1:
			roznica = liczby[0]
			for liczba in liczby[1:]:
				roznica -= liczba
			print (roznica)
			break
		else:
			print ('Lista jest pusta!')
	elif user_input == 'iloczyn':
		iloczyn = 1
		for liczba in liczby:
			iloczyn *= liczba
		print (iloczyn)
		break
	elif user_input == 'iloraz':
		try:
			iloraz = liczby[0]
			for liczba in liczby[1:]:
				iloraz /= liczba
			print (iloraz)
			break
		except ZeroDivisionError:
			print ('Nie mozna dzielic przez zero!')
			break
	else:
		try:
			liczby.append(float(user_input))
		except ValueError:
			print ('Wpisano nieprawidlowa wartosc. Sprobuj ponownie!')



# Czat dodał sprawdzenie czy lista jest pusta, wyjątek dla dzielenia przez zero i komunikat błędu od float
