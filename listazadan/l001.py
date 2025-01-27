# Lista zadań (To-Do List)
# Stwórz aplikację do zarządzania zadaniami, która pozwala użytkownikowi dodawać, usuwać i wyświetlać zadania.

### l001 ###
############

# Witaj w l001!
# add / del / show
# >>

# ostatnio dodane, id, data dodania, status
import shlex
import funky

print ("\n\nWitaj w l001!")

def glowna_funkcja (polecenie):

	if polecenie == 'add': # ADD
		NOTKA = input("Wpisz notatke: ").strip()
		print ("_DONE_")
		print ("## glowna funkcja add")
		pobierz_input()
	elif polecenie == 'del': # DEL
		DEL_ID = input("Podaj id: ").strip().lower()
		print ("_DONE_")
		print ("## glowna funkcja del")
		pobierz_input()
	elif polecenie == 'show': # SHOW
		print ("""\nshow [a] - pokazuje a ostatnich notatek
show - pokazuje 5 ostatnich notatek
show all - pokazuje wszystkie notatki""")
		print ("## glowna funkcja show")
		pobierz_input()
	elif polecenie == 'menu':
		pobierz_input()
	elif polecenie in ['end', 'exit', 'quit', 'q']:
		print ("### program end ###")
	else:
		print ("### nieprawidlowe polecenie! ###")
		print ("polecenie: ",polecenie)
		pobierz_input()

def pobierz_input():
	print ("add / del / show")
	usr_input = shlex.split(input(">> ").strip().lower())
	glowna_funkcja(funky.sprawdz_input(usr_input))

pobierz_input()

