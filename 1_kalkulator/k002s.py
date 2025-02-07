# Kalkulator tekstowy
# Napisz prosty kalkulator, który wykonuje podstawowe działania matematyczne, takie jak dodawanie, odejmowanie, mnożenie i dzielenie.

### k002s ###
#############


liczby = []

while True:
	print ("""
\n
>> suma
>> roznica
>> iloczyn
>> iloraz
>> exit
""")
	print (liczby)
	user_input = input('Wpisz liczbe lub polecenie: ')
	### input check ###
	if user_input.lower() == 'suma':  ### suma ###
		if len(liczby) > 1: # jezeli lista nie jest pusta
			print ('SUMA WYNOSI: ',sum(liczby))
			break
		else:
			print ('Podaj minimum 2 wartosci!')
	elif user_input.lower() == 'roznica': ### roznica ###
		if len(liczby) > 1:
			roznica = liczby[0]
			for liczba in liczby[1:]:
				roznica -= liczba
			print ('ROZNICA WYNOSI: ',roznica)
			break
		else:
			print ('Podaj minimum 2 wartosci!')
	elif user_input.lower() == 'iloczyn': ### iloczyn ###
		if len(liczby) > 1:
			iloczyn = 1
			for liczba in liczby:
				iloczyn *= liczba
			print ('ILOCZYN WYNOSI: ',iloczyn)
			break
		print ('Podaj minimum 2 wartosci!')
	elif user_input.lower() == 'iloraz':  ### iloraz ###
		if len(liczby) > 1:
			try:
				iloraz = liczby[0]
				for liczba in liczby[1:]:
					iloraz /= liczba
				print ('ILORAZ WYNOSI: ',iloraz)
				break
			except ZeroDivisionError:
				print ('Nie mozna dzielic przez zero!')
				break
		else:
			print ('Podaj minimum 2 wartosci!')
	elif user_input.lower() == 'exit': ### exit ###
		break
	else:  ### liczby ###
		try:
			liczby.append(float(user_input))
		except ValueError:
			print ('Wpisano nieprawidlowa wartosc. Sprobuj ponownie!')
