# Lista zadań (To-Do List)
# Stwórz aplikację do zarządzania zadaniami, która pozwala użytkownikowi dodawać, usuwać i wyświetlać zadania.

### l001 ###
############

# Witaj w l001!
# add / del / show
# >>

# ostatnio dodane, id, data dodania, status

print ("\n\n# Witaj w l001!\n# add / del / show")

def sprawdz_input(user_input):
	if user_input == 'add':
		komenda = 'add'
		return komenda
	elif user_input == 'del':
		komenda = 'del'
		return komenda
	elif user_input == 'show':
		komenda = 'show'
		return komenda
	else:
		komenda = 'error'
		return komenda


def glowna_funkcja (a):  # moze (a, b) ?
	if a == 'add':
		print ("glowna_funkcja add")
	elif a == 'del':
		print ("glowna_funkcja del")
	elif a == 'show':
		dane = open('workfile.txt', 'r', encoding="utf-8")
		print (dane.readlines()) # wartosc w nawiasie to ilosc lini
		print ("glowna_funkcja show")
	elif a == 'error':
		print ("nieprawidlowe polecenie!")

user_input = input().strip().lower()
glowna_funkcja(sprawdz_input(user_input))

#
