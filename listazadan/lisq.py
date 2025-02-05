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


print (f"\nWitaj w lisqu!\n{randrange(0,1000)} <- q <- h")


def glowna_funkcja (polecenie):
			### ADD
	if polecenie == 'add':
		NOTKA = str(input("Wpisz notatke: ").strip())
		if len(NOTKA) != 0:
			print ("works")
			pobierz_input()
		else:
			pobierz_input()
	elif polecenie[0] == 'add' and polecenie[1]:
		print ("_DONE_\n### notatka zapisana")
		pobierz_input()
			### DELETE
	elif polecenie == 'del':
		DEL_ID = input("Wpisz id: ").strip().lower()
		print ("_DONE_")
		print ("### notatka usunieta")
		pobierz_input()
	elif polecenie[0] == 'del' and polecenie[1]:
		print ("_DONE_\n### notatka usunieta")
		pobierz_input()
			### SHOW
	elif polecenie in ['show', 's']:
		for line in read_data[-5:]:
			print (line, end='')
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
		print ("\n©liseq is a free and OpenSource notes app for you\n:: enter q for quit\n:: cls for screen cleanup\n:: show or s <- showing last 10 notes\n:: show [t] <- showing t number of notes\n:: show all <- listing all notes\n:: del 035 <- deliting a specific note\n:: del l <- deliting last note\n:: del all <- deleting all notes")
		pobierz_input()
	elif polecenie in ['hey', 'hi', 'hello', 'welcome','yo']:
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

with open('/data/data/com.termux/files/home/kod/5challenge/listazadan/dane.txt', 'r', encoding="utf-8") as DANE:
	read_data = DANE.read()

pobierz_input()

# id_nr =
# data_nr =
