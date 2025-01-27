# Lista zadań (To-Do List)
# Stwórz aplikację do zarządzania zadaniami, która pozwala użytkownikowi dodawać, usuwać i wyświetlać zadania.

### l001 ###
############

# Witaj w l001!
# add / del / show
# >>

# ostatnio dodane, id, data dodania, status

print ("\n\n >> Witaj w l001!\n >> add / del / show")

def sprawdz_input(usr_input):
	if usr_input == 'add':
		komenda = 'add'
		return komenda
	elif usr_input == 'del':
		komenda = 'del'
		return komenda
	elif usr_input == 'show':
		komenda = 'show'
		return komenda
	else:
		komenda = 'error'
		return komenda


def glowna_funkcja (a):  # moze (a, b) ? dystrybutor
	if a == 'add':
		a, b = input().split()
		print (a, b)
		print ("glowna_funkcja add")
	elif a == 'del':
		print ("glowna_funkcja del")
	elif a == 'show':
		dane = open('workfile.txt', 'r', encoding="utf-8")
		print (dane.read()) # wartosc w nawiasie to ilosc lini
		print ("glowna_funkcja show")
	elif a == 'error':
		print ("nieprawidlowe polecenie!")

usr_input = input().strip().lower()
glowna_funkcja(sprawdz_input(usr_input))


# show -all
# show -3
