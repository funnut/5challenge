# Lista zadań (To-Do List)
# Stwórz aplikację do zarządzania zadaniami, która pozwala użytkownikowi dodawać, usuwać i wyświetlać zadania.

### l001 ###
############

# Witaj w l001!
# add / del / show
# >
# ostatnio dodane, id, data dodania, status

from random import randrange
import shlex
import funky


print (f"\n\n\nWitaj w lisku!\n{randrange(0,1000)} <- q <- h")


def glowna_funkcja (polecenie):
	if polecenie == 'add': # ADD
		NOTKA = str(input("Wpisz notatke: ").strip())
		print(NOTKA)
		if len(NOTKA) != 0:
			print ("_DONE_\n### notatka zapisana")
			pobierz_input()
		else:
			pobierz_input()
	elif polecenie[0] == 'add' and polecenie[1]:
		print ("_DONE_\n### notatka zapisana")
		pobierz_input()
			###
	elif polecenie == 'del': # DEL
		DEL_ID = input("Wpisz id: ").strip().lower()
		print ("_DONE_")
		print ("### notatka usunieta")
		pobierz_input()
	elif polecenie[0] == 'del' and polecenie[1]:
		print ("_DONE_\n### notatka usunieta")
		pobierz_input()
			###
	elif polecenie in ['show', 's']: # SHOW
		pobierz_input()
	elif polecenie[0] in ['show', 's'] and polecenie[1] == 'all':
		print (read_data)
		pobierz_input()
	elif polecenie in ['show', 's'] and int(polecenie[1]):
		print ("show [a]")
		pobierz_input()
			###
	elif polecenie in ['cls', 'clear']:
		funky.cleanup()
		pobierz_input()
	elif polecenie in ['help', 'h', 'menu', 'info', 'commands']:
		print ("\n\nLisek is a free and OpenSource notes app for your terminal\nEnter q for quit\ncls for screen cleanup\nshow or s <- showing last 5 notes\nshow [t] <- showing t number of notes\nshow all <- listing all notes\ndel id035 <- deliting a specific note\ndel all <- deleting all notes")
		pobierz_input()
	elif polecenie in ['hey', 'hi', 'hello', 'welcome','yo']
		print ("\nNice having you here!\nShall we start?")
		pobierz_input()
	elif polecenie in ['end', 'exit', 'quit', 'q']:
		print ("### program_end ###")
	else:
		print ("### nieprawidlowe_polecenie! ###")
		print ("var ",polecenie)
		pobierz_input()


def pobierz_input():
	print ("add / del / show")
	usr_input = shlex.split(input(">> ").strip().lower())
	glowna_funkcja(funky.sprawdz_input(usr_input))

with open('dane.txt', 'r', encoding="utf-8") as DANE:
	read_data = DANE.read()

pobierz_input()

