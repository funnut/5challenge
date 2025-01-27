# Lista zadań (To-Do List)
# Stwórz aplikację do zarządzania zadaniami, która pozwala użytkownikowi dodawać, usuwać i wyświetlać zadania.

### l001 ###
############

# Witaj w l001!
# add / del / show
# >>

user_input = input().strip()

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
		komenda = 'eRRor'
		return komenda


def glowna_funkcja (a):  # moze (a, b) ?
	if a == 'add':
		print ("glowna_funkcja add")
	elif a == 'del':
		print ("glowna_funkcja del")
	elif a == 'show':
		print ("glowna_funkcja show")
	elif a == 'eRRor':
		print ("nieprawidlowe polecenie!")

glowna_funkcja(sprawdz_input(user_input))
