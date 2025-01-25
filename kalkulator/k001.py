# 1. Kalkulator tekstowy
# Napisz prosty kalkulator, który wykonuje podstawowe działania matematyczne, takie jak dodawanie, odejmowanie, mnożenie i dzielenie.

##################
### WERSJA_1.0 ###
##################

a = float(input("Podaj A: "))
b = float(input("Podaj B: "))

suma = a + b
print (f"Suma wynosi: {suma}")

roznica = a - b
print (f"Roznica wynosi: {roznica}")

iloczyn = a * b
print (f"Iloczyn wynosi: {iloczyn}")

if b != 0:
	iloraz = a / b
	print (f"Iloraz wynosi: {iloraz}")

	print ('Calkowita czesc z dzielenia: ', a // b)

	modulo = a % b
	print (f"Reszta z dzielenia: {modulo}")
else:
	print ("Nie dzielimy przez 0 !")

print ("Potega wynosi: ", a ** b)
